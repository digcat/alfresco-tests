import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configure import Configuration
import socket

class TestAssertSeleniumFTPservice(unittest.TestCase):
    def setUp(self):
	config = Configuration.from_file('./config.yml').configure()
       	self.url = config['url']
	self.username = config['user']
	self.password = config['passwd']
	self.ftpurl = socket.gethostbyname(config['ftpurl'])
	self.ftpport = config['ftpport']
	self.ftpsrcfile = config['ftpsrcfile']
	self.ftpsrc = config['ftpsrc']
  
  
    def test_SWSDP_FTP_aLogin(self):
	import ftplib
	f = ftplib.FTP()
	f.connect(self.ftpurl,port=self.ftpport)
	f.login(self.username,self.password)
	data = []
	f.dir(data.append)
	f.quit()
	self.assertIn('Alfresco',str(data))


    def test_SWSDP_FTP_findDocument(self):
	import ftplib
        f = ftplib.FTP()
        f.connect(self.ftpurl,port=self.ftpport)
        f.login(self.username,self.password)
	f.cwd(self.ftpsrc)
	data = []
	f.dir(data.append)
	f.quit()
	self.assertIn(self.ftpsrcfile,str(data))
	
	
	
    def tearDown(self):
	self = [] 


if __name__ == '__main__':
    unittest.main()
