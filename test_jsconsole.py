import unittest
from selenium import webdriver

import page
import page_jsconsole
import testconfig

"""  testJSConsoleMyAlfresco """

class testJSConsoleMyAlfresco(unittest.TestCase):
    """ testJSConsoleMyAlfresco Class """

    def setUp(self):
        """ Setup browser and connection """
	self = testconfig.getVars(self)
	self.driver = testconfig.setBrowser(self)
        self.driver.get(self.loginurl)

    def test_JSConsole_alfresco_login(self):
        main_page = page.MainPage(self.driver)
	main_page.click_login_button()
	main_page.photo_page()
        assert main_page.is_title_matches("Dashboard"),"FAIL: didnt make it to dashboard on login ! Check Credentials"
	
    def test_JSConsole_goto_jsconsole(self):
	jsconsole_page = page_jsconsole.JSConsolePage(self.driver)	
	jsconsole_page.click_login_button()
	jsconsole_page.click_jsconsole_button()
        main_page = page.MainPage(self.driver)
	main_page.photo_page()
	assert main_page,is_title_matches("Admin Tools", "FAIL: to reach admin tools page")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
