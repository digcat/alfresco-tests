from element import BasePageElement
from locators import MainPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import inspect
import datetime
import testconfig
import os
import time

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
	for link in element:
		link.click()
   
    def click_searchbudgetform(self):
	vars = testconfig.getVars(self)	
	self.driver.maximize_window()
	element = self.driver.get(vars.url + '/share/page/site/swsdp/advsearch')
	element = self.driver.find_element(*MainPageLocators.SEARCH_FORM)
	element.send_keys('budget.xls')
	element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
	element.click()
	element = self.driver.find_elements_by_link_text('budget.xls')
	for item in element:
			item.click()
	message = self.driver.find_element_by_xpath("//div[contains(@class, 'message')]")
	previewmessage = message.get_attribute('innerHTML')
	return previewmessage.strip()

    def click_create_site_mainmenu(self):
	vars = testconfig.getVars(self)
	element = self.driver.find_element(*MainPageLocators.MAINMENU_SITES)
        element.click()


    def click_create_siteforpreviews(self,sitename):
        vars = testconfig.getVars(self)
        now = datetime.datetime.now()
        today = now.strftime("%H%M%S%y%m%d")
        element = self.driver.find_element(*MainPageLocators.MAINMENU_SITES)
        element.click()
        element = self.driver.find_element(*MainPageLocators.RMCREATESITE_BUTTON)
        element.click()
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(*MainPageLocators.RMCREATESITE_NAME).is_displayed())
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(*MainPageLocators.RMCREATESITE_SUBMIT).is_displayed())
        element = self.driver.find_element(*MainPageLocators.RMCREATESITE_NAME)
        element.click()
        element.send_keys(sitename)
        element = self.driver.find_element_by_name('description')
        element.send_keys('site to test previews')
        element.click()
        #element = self.driver.find_element_by_name('shortName')
        #element.send_keys(sitename)
        element = self.driver.find_element_by_name('sitePreset')
        element.send_keys("C")
        element.click()
        element = self.driver.find_element(*MainPageLocators.RMCREATESITE_SUBMIT)
        element.click()
        element = self.driver.get(vars.url + '/share/page/console/admin-console/manage-sites')

 
    def click_create_site(self):
        vars = testconfig.getVars(self)
        now = datetime.datetime.now()
        today = now.strftime("%H%M%S%y%m%d")
        sitename = today + ' Site'
        element = self.driver.find_element(*MainPageLocators.MAINMENU_SITES)
        element.click()
        element = self.driver.find_element(*MainPageLocators.RMCREATESITE_BUTTON)
        element.click()
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(*MainPageLocators.RMCREATESITE_NAME).is_displayed())
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(*MainPageLocators.RMCREATESITE_SUBMIT).is_displayed())
        element = self.driver.find_element(*MainPageLocators.RMCREATESITE_NAME)
        element.click()
        element.send_keys(sitename)
        element = self.driver.find_element_by_name('description')
        element.send_keys(today + ' free text description')
        element.click()
        element = self.driver.find_element_by_name('shortName')
        element.send_keys(today)
        element = self.driver.find_element_by_name('sitePreset')
        element.send_keys("C")
        element.click()
        element = self.driver.find_element(*MainPageLocators.RMCREATESITE_SUBMIT)
        element.click()
        element = self.driver.get(vars.url + '/share/page/console/admin-console/manage-sites')	

    def click_delete_site(self):
	vars = testconfig.getVars(self)
	#element = self.driver.get(vars.url + '/share/page/console/admin-console/manage-sites')
	#elementattvalue = element.get_attribute('containerNode,textDirNode')

	gotourl = vars.url + '/share/page/console/admin-console/manage-sites'	
	
	page = self.driver.get(gotourl) 
	
	list_of_lists = [[td.text
                  for td in tr.find_elements_by_xpath('td')]
                  for tr in self.driver.find_elements_by_xpath('//tr')]

	rowcount = 0
	sites = []
	siteslist = []
	targetfordelete = []

	for l in list_of_lists:
		rowcount = rowcount + 1
		if len(l)==5:	
			if len(l[0])>0:
				sites = {'sitename': l[0], 'sitedesc': l[1], 'item1': l[2], 'item2': l[3],'action': l[4], 'row': rowcount}	
				siteslist.append(sites)
				target = l[0]
					
				if "Records Management" in target:
					targetfordelete.append(rowcount)
				if target[0:9].isnumeric() and "Site" in target:
					targetfordelete.append(rowcount) 

	print siteslist	
	print targetfordelete
	document = '\u25be'
	elements = self.driver.find_elements_by_xpath("//span[contains(., \"" + document + "\")]")

	self.mouse = webdriver.ActionChains(self.driver)

	value = 'uniqName'
	actionrow = 0
	for ac in elements:
		actionrow = actionrow + 1
		print actionrow,ac
		if str(actionrow) in targetfordelete:
			ac.click()
			self.driver.mouse.move_to_element(ac.find_element_by_name('Delete').click.perform())

    def click_admin_user_groups_browse(self):
	vars = testconfig.getVars(self)
	element = self.driver.find_element(*MainPageLocators.AC_GROUP_INPUT)
	element.send_keys('SITE_CREATORS')
	element = self.driver.find_element(*MainPageLocators.AC_GROUP_BROWSE)
	element.click()
	try:
		element = self.driver.find_element(*MainPageLocators.AC_GROUP_SSCMEMBERS)
		element.click()
	except:
		return "No Group"
	return "Group found"

    def click_admin_user_groups(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/console/admin-console/groups')			
	WebDriverWait(self.driver, 10).until(lambda s: s.find_element(*MainPageLocators.AC_GROUP_BROWSE).is_displayed())

	
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
	funccallername = inspect.currentframe().f_back.f_code.co_name 	
        pathname = vars.photopath + '/' + funccallername + '.png'
	if ( os.path.exists(pathname)):
		pathname = vars.photopath + '/' + funccallername + '1.png'		  
		if ( os.path.exists(pathname)):
			pathname = vars.photopath + '/' + funccallername + '2.png'	
			if ( os.path.exists(pathname)):
				pathname = vars.photopath + '/' + funccallername + '3.png'	
				if ( os.path.exists(pathname)):
					pathname = vars.photopath + '/' + funccallername + '4.png'	
					if ( os.path.exists(pathname)):
						pathname = vars.photopath + '/' + funccallername + '5.png'	
		
	self.driver.save_screenshot(pathname)   
