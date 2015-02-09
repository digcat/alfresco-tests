import socket
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configure import Configuration
import imaplib, email

class TestAssertSeleniumIMAPservice(unittest.TestCase):
    def setUp(self):
	config = Configuration.from_file('./config.yml').configure()
       	self.url = config['url']
	self.username = config['user']
	self.password = config['passwd']
	self.imap_host = config['imap_host']
	self.imap_port = config['imap_port']
	
	
    def test_SWSDP_IMAP_OpenConnection(self):
	reponame = ''
	mboxes = []
	try:
		server = imaplib.IMAP4(self.imap_host,self.imap_port)
		serverconn = "OK" 
	except:
		serverconn = "FAILED"

	if serverconn == "OK":
		try:
			server.login(self.username,self.password)
			loginconn = "OK"
		except:
			loginconn = "FAILED"
	
		mboxes = server.list()[1]
		#for mbox in mboxes:
		#	print mbox
			
	
	self.assertIn("Alfresco IMAP",str(mboxes))
	
    def tearDown(self):
	self = [] 


if __name__ == '__main__':
   unittest.main()
