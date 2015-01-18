import unittest
from configure import Configuration
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class testLoggedIn(unittest.TestCase):
    def setUp(self):
	config = Configuration.from_file('./config.yml').configure()
        self.browser = webdriver.Firefox()
       	self.url = config['url']
	self.username = config['user']
	self.password = config['passwd']
	url = self.url + '/share'
	self.browser.get(url)
	finallycomplete = 0	
	try:
		element = WebDriverWait(self.browser, 120).until(
			EC.presence_of_element_located((By.ID, "page_x002e_components_x002e_slingshot-login_x0023_default-username"))
		)
	finally:
		finallycomplete = 1
	
	driver = self.browser	
	elem = driver.find_element_by_name('username')
        elem.send_keys(self.username)
        elem = driver.find_element_by_name('password')
        elem.send_keys(self.password)
        elem.submit()
	try:	
		element = WebDriverWait(driver, 180).until(
			EC.presence_of_element_located((By.ID, "HEADER_SITE_MEMBERS"))
		)
	finally:
		finallycomplete = 1

    def test_SWSDP_EditProperties(self):
	picture = self.url + '/share/page/site/swsdp/edit-metadata?nodeRef=workspace://SpacesStore/0f672fb8-bbdb-41bb-84f3-7b9bb1c39b30'
       	self.browser.get(picture)
	try:
		element = WebDriverWait(self.browser,30).until(
			EC.presence_of_element_located((By.ID,"HEADER_SEARCH_BOX"))
		)
	finally:
		self.assertIn("Edit Properties",self.browser.title)

    def test_SWSDP_PeopleFinder(self):
	url = self.url + '/share/page/people-finder'	
	self.browser.get(url)
	try:
		element = WebDriverWait(self.browser,30).until(
			EC.presence_of_element_located((By.ID,"HEADER_SEARCH_BOX"))
		)
	finally:
		self.assertIn("People Finder",self.browser.title)

    def test_SWSDP_DocumentLibrary(self):
	url = self.url + '/share/page/site/swsdp/documentlibrary'
	self.browser.get(url)
	try:
		element = WebDriverWait(self.browser,30).until(
			EC.presence_of_element_located((By.ID,"HEADER_SEARCH_BOX"))
		)
	finally:
		self.assertIn("Project Library",self.browser.title)
	
    def test_SWSDP_MyTasks(self):
	url = self.url + '/share/page/my-tasks'
	self.browser.get(url)
	try:
		element = WebDriverWait(self.browser,30).until(
			EC.presence_of_element_located((By.ID,"HEADER_SEARCH_BOX"))
		)
	finally:
		self.assertIn("My Tasks",self.browser.title)

    def test_SWSDP_ProjectWiki(self):
	url = self.url + '/share/page/site/swsdp/wiki-page'
	self.browser.get(url)
	try:
		element = WebDriverWait(self.browser,30).until(
			EC.presence_of_element_located((By.ID,"HEADER_SEARCH_BOX"))
		)
	finally:
		self.assertIn("Project Wiki",self.browser.title)	
	
    def test_SWSDP_ProjectDataLists(self):
	url = self.url + '/share/page/site/swsdp/data-lists'
	self.browser.get(url)
	try:
		element = WebDriverWait(self.browser,30).until(
			EC.presence_of_element_located((By.ID,"HEADER_SEARCH_BOX"))
		)
	finally:
		self.assertIn("Project Lists",self.browser.title)	
    
    def test_SWSDP_ProjectDiscussionLists(self):
	url = self.url + '/share/page/site/swsdp/discussions-topiclist'
	self.browser.get(url)
	try:
		element = WebDriverWait(self.browser,30).until(
			EC.presence_of_element_located((By.ID,"HEADER_SEARCH_BOX"))
		)
	finally:
		self.assertIn("Project FAQ",self.browser.title)	
    
    def test_SWSDP_ProjectLinks(self):
	url = self.url + '/share/page/site/swsdp/links'
	self.browser.get(url)
	try:
		element = WebDriverWait(self.browser,30).until(
			EC.presence_of_element_located((By.ID,"HEADER_SEARCH_BOX"))
		)
	finally:
		self.assertIn("Project Links",self.browser.title)
    

    def tearDown(self):
	logout = self.url + '/share/page/dologout'
	self.browser.get(logout)
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=3)
