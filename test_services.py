import unittest
from selenium import webdriver

import page
import testconfig

"""  TestServicesMyAlfresco """

class testServicesMyAlfresco(unittest.TestCase):
    """ testServicesMyAlfresco Class """

    def setUp(self):

        """ Setup browser and connection """
	self = testconfig.getVars(self)
	self.driver = testconfig.setBrowser(self)
	self.driver.get(self.loginurl)

    def test_services_delete_site(self):
        main_page = page.MainPage(self.driver)
	main_page.click_login_button()
	main_page.click_delete_site()
        assert main_page.is_title_matches("Dashboard"),"FAIL: didnt make it to dashboard on login ! Check Credentials"
		
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
