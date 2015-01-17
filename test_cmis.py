import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configure import Configuration
import socket
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
	except:
		repo = [] 
	if len(str(repo))>0:
		repoid = repo.getRepositoryId() 
		self.assertIn('a',repoid)
	
    def tearDown(self):
	self = [] 


if __name__ == '__main__':
    unittest.main(verbosity=3)
