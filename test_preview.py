import unittest
from selenium import webdriver

import page
import testconfig
import fast_selenium

"""  Test PreviewAlfresco """
"""  Author: DigCat.com """

class testPreviewAlfresco(unittest.TestCase):
    """ testPreviewAlfresco Class """

    def setUp(self):

        """ Setup browser and connection """
        self = testconfig.getVars(self)
        self.driver = testconfig.setBrowser(self)
        self.driver.get(self.loginurl)
        if "Alfresco" not in self.driver.title:
            raise Exception("Cant get to login page")

    def test_alfresco_login(self):
        print "Login"
        main_page = page.MainPage(self.driver)
        main_page.click_login_button()
        assert main_page.is_title_matches("Dashboard"),"FAIL: didnt make it to dashboard on login ! Check Credentials"
	
    def test_alfresco_goto_searchsolr(self):
        print "Search solr"
        main_page = page.MainPage(self.driver)
        main_page.click_login_button()
        outcome = main_page.click_searchbudgetform()
        badoutcome = "This document can't be previewed."
        if badoutcome in outcome:
            raise Exception("No Preview Possible")
 	
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
