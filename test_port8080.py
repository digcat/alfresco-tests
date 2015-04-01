import unittest
from selenium import webdriver

import page
import page_jsconsole
import testconfig
import fast_selenium

"""  testPort8080MyAlfresco """

class testPort8080MyAlfresco(unittest.TestCase):
    """ testPort8080MyAlfresco Class """

    def setUp(self):
        """ Setup browser and connection """
	self = testconfig.getVars(self)
	self.driver = testconfig.setBrowser(self)
	
    def test_Port8080_goto_port8080(self):
	self.driver.get(self.host + ':8080')	
	assert "Problem loading page" in self.driver.title

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
