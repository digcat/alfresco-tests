import unittest, time
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
		element = WebDriverWait(driver, 340).until(
			EC.presence_of_element_located((By.ID, "global_x002e_footer"))
		)
	finally:
		finallycomplete = 1

    def test_SWSDP_Search(self):
	self.browser.get(self.url + '/share')
	finallycomplete = 0
	try:
		element = WebDriverWait(self.browser, 120).until(
			EC.presence_of_element_located((By.ID, "HEADER_SEARCHBOX_FORM_FIELD"))
		)
	finally:
		finallycomplete = 1	

	element.send_keys('meetings')

	try:
		element = WebDriverWait(self.browser,5).until(
			EC.presence_of_element_located((By.ID,"uniqName_1_7"))
		)
	finally:
		finallycomplete = 1

	self.assertIn('1',str(finallycomplete))
		

    def tearDown(self):
	logout = self.url + '/share/page/dologout'
	self.browser.get(logout)
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=3)
