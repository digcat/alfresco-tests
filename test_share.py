import unittest
from selenium import webdriver

import page
import testconfig

"""  Test MyAlfresco """
"""  Author: DigCat.com """

class testMyAlfresco(unittest.TestCase):
    """ testMyAlfresco Class """

    def setUp(self):

        """ Setup browser and connection """
	self = testconfig.getVars(self)
	self.driver = testconfig.setBrowser(self)
        self.driver.get(self.loginurl)

    def test_alfresco_login(self):
        main_page = page.MainPage(self.driver)
	main_page.click_login_button()
	main_page.photo_page()
        assert main_page.is_title_matches("Dashboard"),"FAIL: didnt make it to dashboard on login ! Check Credentials"
	
    def test_alfresco_goto_peoplefinder(self):
        main_page = page.MainPage(self.driver)
	main_page.click_login_button()
	main_page.click_people_finder()
	main_page.photo_page()
	assert main_page,is_title_matches("People", "FAIL: to reach the People page")
    
    def test_alfresco_goto_mytasks(self):
        main_page = page.MainPage(self.driver)
	main_page.click_login_button()
	main_page.click_mytasks()
	main_page.photo_page()
	assert main_page,is_title_matches("My Tasks", "FAIL: to reach the My Tasks Page")
    
    def test_alfresco_goto_repository(self):
        main_page = page.MainPage(self.driver)
	main_page.click_login_button()
	main_page.click_repository()
	main_page.photo_page()
	assert main_page,is_title_matches("Repository Browser","FAIL: to reach the Repository Page")

    def test_alfresco_goto_myfiles(self):
        main_page = page.MainPage(self.driver)
	main_page.click_login_button()
	main_page.click_myfiles()
	main_page.photo_page()
	assert main_page,is_title_matches("My Files","FAIL: to reach the Myfiles Page")
    
    def test_alfresco_goto_sharedfiles(self):
        main_page = page.MainPage(self.driver)
	main_page.click_login_button()
	main_page.click_sharedfiles()
	main_page.photo_page()
	assert main_page,is_title_matches("Shared Files", "FAIL: to reach Shared Files Page")

    def test_alfresco_goto_sws_dashboard(self):
        main_page = page.MainPage(self.driver)
	main_page.click_login_button()
	main_page.click_swsdp_dashboard()
	main_page.photo_page()
	assert main_page,is_title_matches("Site Dashboard", "FAIL: to reach SWS Dashboard page")
	
    def test_alfresco_goto_sws_documentlibrary(self):
        main_page = page.MainPage(self.driver)
	main_page.click_login_button()
	main_page.click_swsdp_documentlibrary()
	main_page.photo_page()
	assert main_page,is_title_matches("Project Libary", "FAIL: to reach SWS project library page")
	
    def test_alfresco_goto_sws_memberlist(self):
        main_page = page.MainPage(self.driver)
	main_page.click_login_button()
	main_page.click_swsdp_memberlist()
	main_page.photo_page()
	assert main_page,is_title_matches("Site Members", "FAIL: to reach SWS member list page")

    def test_alfresco_goto_searchsolr(self):
        main_page = page.MainPage(self.driver)
	main_page.click_login_button()
	main_page.click_searchform()
	main_page.photo_page()
	assert main_page,is_title_matches("Search", "FAIL: to reach search result page")
	
    def test_alfresco_create_site(self):
        main_page = page.MainPage(self.driver)
	main_page.click_login_button()
	sites = 2 
	a=0
	while a < sites:
		main_page.click_create_site()
		a = a + 1
	main_page.photo_page()
	assert main_page,is_title_matches("Site Dashboard","FAIL: to reach new site page")
     
#    def test_alfresco_delete_site(self):
#       main_page = page.MainPage(self.driver)
#	main_page.click_login_button()
#	main_page.click_delete_site()
#	main_page.photo_page()
#	assert main_page,is_title_matches("Sites Manager","FAIL: to delete site")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
