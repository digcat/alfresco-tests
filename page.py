

from element import BasePageElement
from locators import MainPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import inspect
import datetime
import testconfig
import os

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    def is_title_matches(self,string):
        return string in self.driver.title
    
    def click_login_button(self):
	vars = testconfig.getVars(self)	
	element = self.driver.find_element_by_name('username')
	element.send_keys(vars.username)
	element = self.driver.find_element_by_name('password')
	element.send_keys(vars.password)
	element.submit()
    
    def click_searchform(self):
	vars = testconfig.getVars(self)	
	element = self.driver.get(vars.url + '/share/page/site/swsdp/advsearch')
	element = self.driver.find_element(*MainPageLocators.SEARCH_FORM)
	element.send_keys('meetings')
	element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
	element.click()
    
    def click_create_site(self):
	vars = testconfig.getVars(self)	
	now = datetime.datetime.now()
	today = now.strftime("%H%M%y%m%d") 
	sitename = today + ' Site'
	element = self.driver.find_element(*MainPageLocators.MAINMENU_SITES)
	element.click()
	element = self.driver.find_element(*MainPageLocators.RMCREATESITE_BUTTON)
	element.click()
	element = self.driver.find_element(*MainPageLocators.RMCREATESITE_NAME)
	element.click()
        element = self.driver.find_element_by_id('alfresco-rm-createSite-instance-ok-button-button')
	element = self.driver.find_element_by_name('title')
	element.send_keys(sitename)
	element.click()
	element = self.driver.find_element_by_name('description')
	element.send_keys(today + ' free text description')
	element.click()
	#element = self.driver.find_element_by_name('shortName')
	#element.send_keys(today)
	element = self.driver.find_element_by_name('sitePreset')
	element.send_keys("C")
	element.click()
	element = self.driver.find_element_by_id('alfresco-rm-createSite-instance-ok-button-button')
	element.click()
	element = self.driver.get(vars.url + '/share/page/console/admin-console/manage-sites')
	

    def click_delete_site(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/console/admin-console/manage-sites')
	elementattvalue = element.get_attribute('containerNode,textDirNode')
	print format(elementattvalue)

	element = self.driver.find_element(*MainPageLocators.AC_DEL_REMOVE)
	element.click()
	element = self.driver.find_element(*MainPageLocators.AC_DEL_DELETE)
	element.click()
			
	element = self.driver.find_element(*MainPageLocators.AC_DEL_CONFIRM)
	element.click()
	
    def click_people_finder(self):
	vars = testconfig.getVars(self)	
	element = self.driver.get(vars.url + '/share/page/people-finder')
    
    def click_mytasks(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/my-tasks')

    def click_repository(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/repository')

    def click_myfiles(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/context/mine/myfiles')
    
    def click_sharedfiles(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/context/shared/sharedfiles')
	
    def click_swsdp_dashboard(self):
	vars = testconfig.getVars(self)	
	element = self.driver.get(vars.url + '/share/page/site/swsdp/dashboard')

    def click_swsdp_documentlibrary(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/site/swsdp/documentlibrary')
    
    def click_swsdp_memberlist(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/site/swsdp/site-members')

    def photo_page(self):
	vars = testconfig.getVars(self)
	if (len(vars.photopath)==0):
		return

	try:
		os.makedirs(vars.photopath)
	except OSError:
		if os.path.exists(vars.photopath):
			pass
		else:
			raise	

	if ( os.path.exists(vars.photopath)):
		pathready = True		
	else:
		mkdir(vars.photopath)
		pathready = True
		
        pathname = vars.photopath + '/' + inspect.currentframe().f_back.f_code.co_name + '.png'
	self.driver.save_screenshot(pathname)   
