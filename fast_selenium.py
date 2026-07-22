# Copyright 2013 BrowserStack

import base64
import http.client as httplib
import logging
import socket

from selenium.webdriver.remote import utils
from selenium.webdriver.remote.errorhandler import ErrorCode
from selenium.webdriver.remote.webdriver import RemoteConnection

try:
    from urllib.request import parse
except ImportError:
    pass

LOGGER = logging.getLogger(__name__)


class BsRemoteConnection(RemoteConnection):
    """
    A connection with the Remote WebDriver server.

    Communicates with the server using the WebDriver wire protocol:
    http://code.google.com/p/selenium/wiki/JsonWireProtocol
    """

    # akshay:ryan@127.0.0.1:4444
    def __init__(self, remote_server_addr):
        # Attempt to resolve the hostname and get an IP address.
        super().__init__(remote_server_addr)
        parsed_url = parse.urlparse(remote_server_addr)
        addr = ""
        if parsed_url.hostname:
            try:
                netloc = socket.gethostbyname(parsed_url.hostname)
                addr = netloc
                if parsed_url.port:
                    netloc += ":%d" % parsed_url.port
                if parsed_url.username:
                    auth = parsed_url.username
                    if parsed_url.password:
                        auth += f":{parsed_url.password}"
                    netloc = f"{auth}@{netloc}"
            except socket.gaierror:
                LOGGER.info(f"Could not get IP address for host: {parsed_url.hostname}")

        # SECURITY FIX: Support HTTPS connections
        if parsed_url.scheme == "https":
            self._conn = httplib.HTTPSConnection(str(addr), str(parsed_url.port or 443))
        else:
            self._conn = httplib.HTTPConnection(str(addr), str(parsed_url.port or 80))

    def _request(self, url, data=None, method=None):
        """
        Send an HTTP request to the remote server.

        :Args:
         - method - A string for the HTTP method to send the request with.
         - url - The URL to send the request to.
         - body - The message body to send.

        :Returns:
          A dictionary with the server's parsed JSON response.
        """
        LOGGER.debug(f"{method} {url} {data}")

        parsed_url = parse.urlparse(url)
        auth_params, addr_port = parsed_url.netloc.split("@")
        headers = {}
        headers["Connection"] = "Keep-Alive"
        headers[method] = parsed_url.path
        headers["User-Agent"] = "Python http auth"
        headers["Content-type"] = 'text/html;charset="UTF-8"'
        headers["Connection"] = "keep-alive"

        # for basic auth
        if parsed_url.username:
            # SECURITY FIX: Proper base64 encoding for Python 3
            auth_string = f"{parsed_url.username}:{parsed_url.password}"
            auth = (
                base64.standard_b64encode(auth_string.encode("utf-8"))
                .decode("ascii")
                .replace("\n", "")
            )
            # Authorization header
            headers["Authorization"] = f"Basic {auth}"

        self._conn.request(method, parsed_url.path, data, headers)
        resp = self._conn.getresponse()
        statuscode = resp.status
        statusmessage = resp.msg
        LOGGER.debug(f"{statuscode} {statusmessage}")
        data = resp.read()
        try:
            if statuscode > 399 and statuscode < 500:
                return {"status": statuscode, "value": data}
            body = data.decode("utf-8").replace("\x00", "").strip()
            content_type = []
            if resp.getheader("Content-Type") is not None:
                content_type = resp.getheader("Content-Type").split(";")
            if not any(x.startswith("image/png") for x in content_type):
                try:
                    data = utils.load_json(body.strip())
                except ValueError:
                    if statuscode > 199 and statuscode < 300:
                        status = ErrorCode.SUCCESS
                    else:
                        status = ErrorCode.UNKNOWN_ERROR
                    return {"status": status, "value": body.strip()}

                assert type(data) is dict, f"Invalid server response body: {body}"
                assert "status" in data, f"Invalid server response; no status: {body}"
                # Some of the drivers incorrectly return a response
                # with no 'value' field when they should return null.
                if "value" not in data:
                    data["value"] = None
                return data
            else:
                data = {"status": 0, "value": body.strip()}
                return data
        finally:
            LOGGER.debug("Finished Request")


from selenium.webdriver.remote import webdriver

webdriver.RemoteConnection = BsRemoteConnection
