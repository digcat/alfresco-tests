import unittest
from selenium import webdriver

import page
import testconfig
import fast_selenium

"""  testShareSiteCreatorsMyAlfresco """

class testShareSiteCreatorsMyAlfresco(unittest.TestCase):
    """ testShareSiteCreatorsMyAlfresco Class """

    def setUp(self):
	self = testconfig.getVars(self)
        """ Setup browser and connection """
	self.driver = testconfig.setBrowser(self)
	self.driver.get(self.loginurl)

    def test_shareSiteCreator_groups(self):
        main_page = page.MainPage(self.driver)
	main_page.click_login_button()
	main_page.click_admin_user_groups()
	grptest = main_page.click_admin_user_groups_browse()
	main_page.photo_page()
	sitetest = ''
	try:
		main_page.click_create_site_mainmenu()
		main_page.photo_page()
		sitetest = 'Site Created'
	except:
		sitetest = 'No Site'
        
	assert ("No Site" in sitetest ),"FAIL: Site has been created! with scg enabled"
		
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
