
from selenium.webdriver.common.by import By

import testconfig


class JSConsoleBasePage:

    def __init__(self, driver):
        self.driver = driver


class JSConsolePage(JSConsoleBasePage):
    def is_title_matches(self, string):
        return string in self.driver.title

    def click_login_button(self):
        vars = testconfig.getVars(self)
        element = self.driver.find_element(By.NAME, "username")
        element.send_keys(vars.username)
        element = self.driver.find_element(By.NAME, "password")
        element.send_keys(vars.password)
        element.submit()

    def click_jsconsole_button(self):
        vars = testconfig.getVars(self)
        self.driver.get(vars.url + "/share/page/console/admin-console/javascript-console")
