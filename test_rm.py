import unittest
from selenium import webdriver

import page
import page_rm
import testconfig
import fast_selenium

"""  Test MyAlfresco """
"""  Author: DigCat.com """

class testRecordManagementMyAlfresco(unittest.TestCase):
    """ testRecordManagementMyAlfresco Class """

    def setUp(self):

        """ Setup browser and connection """
	self = testconfig.getVars(self)
	self.driver = testconfig.setBrowser(self)
        self.driver.get(self.loginurl)

    def test_RM_alfresco_login(self):
        main_page = page.MainPage(self.driver)
	main_page.click_login_button()
	main_page.photo_page()
        assert main_page.is_title_matches("Dashboard"),"FAIL: didnt make it to dashboard on login ! Check Credentials"
	
    def test_RM_create_site(self):
	rm_page = page_rm.RMPage(self.driver)	
        rm_page.click_login_button()
        rm_page.click_create_recordsmanagement_button()
        main_page = page.MainPage(self.driver)
        main_page.photo_page()
        assert rm_page,is_title_matches("Site Dashboard","FAIL: to reach new site page")

    def test_RM_goto_peoplefinder(self):
        main_page = page.MainPage(self.driver)
	main_page.click_login_button()
	main_page.click_people_finder()
	main_page.photo_page()
	assert main_page,is_title_matches("People", "FAIL: to reach the People page")

    def test_RM_goto_rm_tools(self):
	rm_page = page_rm.RMPage(self.driver)	
	rm_page.click_login_button()
	rm_page.click_rm_tools_button()
        main_page = page.MainPage(self.driver)
	main_page.photo_page()
	assert main_page,is_title_matches("RM Admin Tools", "FAIL: to reach RM admin tools page")

    def test_RM_goto_rm_tools_audit(self):
        rm_page = page_rm.RMPage(self.driver)
        rm_page.click_login_button()
        rm_page.click_rm_tools_audit_button()
        main_page = page.MainPage(self.driver)
        main_page.photo_page()
        assert main_page,is_title_matches("RM Admin Tools", "FAIL: to reach RM admin tools page")

    def test_RM_goto_rm_tools_custom_metadata(self):
        rm_page = page_rm.RMPage(self.driver)
        rm_page.click_login_button()
        rm_page.click_rm_tools_custom_metadata_button()
        main_page = page.MainPage(self.driver)
        main_page.photo_page()
        assert main_page,is_title_matches("RM Admin Tools", "FAIL: to reach RM admin tools page")

    def test_RM_goto_rm_tools_define_roles(self):
        rm_page = page_rm.RMPage(self.driver)
        rm_page.click_login_button()
        rm_page.click_rm_tools_define_roles_button()
        main_page = page.MainPage(self.driver)
        main_page.photo_page()
        assert main_page,is_title_matches("RM Admin Tools", "FAIL: to reach RM admin tools page")

    def test_RM_goto_rm_tools_email_mappings(self):
        rm_page = page_rm.RMPage(self.driver)
        rm_page.click_login_button()
        rm_page.click_rm_tools_email_mappings_button()
        main_page = page.MainPage(self.driver)
        main_page.photo_page()
        assert main_page,is_title_matches("RM Admin Tools", "FAIL: to reach RM admin tools page")

    def test_RM_goto_rm_tools_events(self):
        rm_page = page_rm.RMPage(self.driver)
        rm_page.click_login_button()
        rm_page.click_rm_tools_events_button()
        main_page = page.MainPage(self.driver)
        main_page.photo_page()
        assert main_page,is_title_matches("RM Admin Tools", "FAIL: to reach RM admin tools page")
   
    def test_RM_goto_rm_tools_list_of_values(self):
        rm_page = page_rm.RMPage(self.driver)
        rm_page.click_login_button()
        rm_page.click_rm_tools_list_of_values_button()
        main_page = page.MainPage(self.driver)
        main_page.photo_page()
        assert main_page,is_title_matches("RM Admin Tools", "FAIL: to reach RM admin tools page")
     
    def test_RM_goto_rm_tools_references(self):
        rm_page = page_rm.RMPage(self.driver)
        rm_page.click_login_button()
        rm_page.click_rm_tools_references_button()
        main_page = page.MainPage(self.driver)
        main_page.photo_page()
        assert main_page,is_title_matches("RM Admin Tools", "FAIL: to reach RM admin tools page")
    
    def test_RM_goto_rm_user_rights(self):
        rm_page = page_rm.RMPage(self.driver)
        rm_page.click_login_button()
        rm_page.click_rm_tools_user_rights_button()
        main_page = page.MainPage(self.driver)
        main_page.photo_page()
        assert main_page,is_title_matches("RM Admin Tools", "FAIL: to reach RM admin tools page")
    
    def test_RM_goto_rm_user_and_groups(self):
        rm_page = page_rm.RMPage(self.driver)
        rm_page.click_login_button()
        rm_page.click_rm_tools_user_and_groups_button()
        main_page = page.MainPage(self.driver)
        main_page.photo_page()
        assert main_page,is_title_matches("RM Admin Tools", "FAIL: to reach RM admin tools page")

    def test_RM_goto_rm_search(self):
        rm_page = page_rm.RMPage(self.driver)
        rm_page.click_login_button()
        rm_page.click_rm_search_button()
        main_page = page.MainPage(self.driver)
        main_page.photo_page()
        assert main_page,is_title_matches("Records Search", "FAIL: to reach RM search page")
    
	
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
