import unittest
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
        client = CmisClient(self.cmisatom,'admin','admin')
        repo = client.defaultRepository
        reponame = repo.name	
        print reponame
        print self.cmisatom
        self.assertIn(reponame,"Main Repository"),"FAIL: Didnt make it to main repository"

    def tearDown(self):
        print self

if __name__ == "__main__":
    unittest.main()
