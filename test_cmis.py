import socket
import unittest
import cmislib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configure import Configuration
from cmislib.model import CmisClient, Repository

class TestAssertSeleniumCMISservice(unittest.TestCase):
    def setUp(self):
	config = Configuration.from_file('./config.yml').configure()
       	self.url = config['url']
	self.username = config['user']
	self.password = config['passwd']
	self.cmisurl = config['cmisurl']
	
	
    def test_SWSDP_CMIS_OpenConnection(self):
	client = CmisClient(self.url + self.cmisurl, self.username, self.password) 
	try:
 		repo = client.getDefaultRepository()
		repoid = repo.getRepositoryId() 
	except:
		repo = [] 
		repoid = ''
		repo.name = ''

	self.assertIn('Main Repository',repo.name)
	
    def tearDown(self):
	self = [] 


if __name__ == '__main__':
    unittest.main(verbosity=3)
