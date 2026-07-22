"""
Configuration management for Alfresco test suite.

This module provides configuration loading from config.yml with environment
variable overrides for sensitive credentials.
"""

import os
from selenium import webdriver
from configure import Configuration


class TestConfig:
    """
    Singleton configuration manager for Alfresco tests.

    Loads configuration from config.yml and environment variables.
    Environment variables take precedence over config file values.
    """
    _instance = None

    def __init__(self):
        """Initialize config from config.yml and environment variables."""
        config = Configuration.from_file('./config.yml').configure()

        # Browser configuration
        self.testbrowser = config['browser']

        # Server configuration
        self.sharehost = config['sharehost']
        self.shareport = config['shareport']
        self.repohost = config['repohost']
        self.repoport = config['repoport']
        self.host = config['sharehost']

        # Protocol configuration
        uri = 'https' if config.get('https', True) else 'http'

        # Build URLs
        if self.shareport:
            self.url = f"{uri}://{self.sharehost}:{self.shareport}"
        else:
            self.url = f"{uri}://{self.sharehost}"

        if self.repoport:
            self.repourl = f"{uri}://{self.repohost}:{self.repoport}"
        else:
            self.repourl = f"{uri}://{self.repohost}"

        # SECURITY: Load credentials from environment variables first
        # Falls back to config.yml if not set (for backwards compatibility)
        self.username = os.getenv('ALFRESCO_USER', config.get('user', ''))
        self.password = os.getenv('ALFRESCO_PASSWORD', config.get('passwd', ''))

        if not self.username or not self.password:
            raise ValueError(
                "Credentials must be set via ALFRESCO_USER and ALFRESCO_PASSWORD "
                "environment variables or in config.yml"
            )

        # Additional configuration
        self.loginurl = self.url + config['loginurl']
        self.photopath = config.get('photopath', 'images')
        self.cmisurl = config['cmisurl']
        self.cmisatom = self.repourl + config['cmisatom']
        self.ftpurl = config['sharehost']
        self.ftpport = config.get('ftpport', 21)
        self.imap_host = config.get('imap_host', 'localhost')
        self.imap_port = config.get('imap_port', 143)

    @classmethod
    def get_instance(cls):
        """
        Get or create singleton instance.

        Returns:
            TestConfig: The singleton configuration instance
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


def getVars(self):
    """
    DEPRECATED: Legacy function for backwards compatibility.

    This function modifies the test instance which is an anti-pattern.
    Use TestConfig.get_instance() instead.

    Will be removed in a future version after all tests are migrated to pytest.
    """
    config = TestConfig.get_instance()

    # Copy config attributes to test instance
    self.testbrowser = config.testbrowser
    self.host = config.host
    self.port = config.shareport
    self.sharehost = config.sharehost
    self.shareport = config.shareport
    self.repohost = config.repohost
    self.repoport = config.repoport
    self.url = config.url
    self.repourl = config.repourl
    self.username = config.username
    self.password = config.password
    self.loginurl = config.loginurl
    self.photopath = config.photopath
    self.cmisurl = config.cmisurl
    self.cmisatom = config.cmisatom
    self.ftpurl = config.ftpurl
    self.ftpport = config.ftpport
    self.imap_host = config.imap_host
    self.imap_port = config.imap_port

    return self


def setBrowser(config_or_self):
    """
    Initialize WebDriver based on browser configuration.

    Args:
        config_or_self: Either a TestConfig instance or a test instance (legacy)

    Returns:
        WebDriver: Configured Selenium WebDriver instance
    """
    # Support both new (TestConfig) and old (test instance) patterns
    if isinstance(config_or_self, TestConfig):
        browser = config_or_self.testbrowser
    else:
        browser = config_or_self.testbrowser

    if browser == 'firefox':
        return webdriver.Firefox()
    elif browser == 'chrome':
        return webdriver.Chrome()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
