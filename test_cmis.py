import unittest
import os
from selenium import webdriver
import page
import testconfig
import fast_selenium

from cmislib.model import CmisClient, Repository

"""  testCMISMyAlfresco """

class testCMISMyAlfresco(unittest.TestCase):
    """ testCMISMyAlfresco Class """

    def setUp(self):
        """ Setup browser and connection """
        self = testconfig.getVars(self)

    def test_CMIS_alfresco_login(self):
        # SECURITY FIX: Use credentials from environment variables or testconfig
        username = os.getenv('ALFRESCO_USER', self.username)
        password = os.getenv('ALFRESCO_PASSWORD', self.password)
        client = CmisClient(self.cmisatom, username, password)
        repo = client.defaultRepository
        reponame = repo.name	
        print (reponame)
        print (self.cmisatom)
        self.assertIn(reponame,"Main Repository"),"FAIL: Didnt make it to main repository"

    def tearDown(self):
        print (self)

if __name__ == "__main__":
    unittest.main()
