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

class JSConsoleBasePage(object):

    def __init__(self, driver):
        self.driver = driver

class JSConsolePage(JSConsoleBasePage):
    def is_title_matches(self,string):
        return string in self.driver.title

    def click_login_button(self):
        vars = testconfig.getVars(self)
        element = self.driver.find_element_by_name('username')
        element.send_keys(vars.username)
        element = self.driver.find_element_by_name('password')
        element.send_keys(vars.password)
        element.submit()

    def click_jsconsole_button(self):
	vars = testconfig.getVars(self)
	element = self.driver.get(vars.url + '/share/page/console/admin-console/javascript-console')
