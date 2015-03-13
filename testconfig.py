from configure import Configuration
from selenium import webdriver

""" Collect params from config.yml """
def getVars(self):
	""" Used at setup of test """
	config = Configuration.from_file('./config.yml').configure()
		
	self.testbrowser  = config['browser']
	self.url      	  = config['url']
	self.username 	  = config['user']
	self.password 	  = config['passwd']
	self.loginurl  	  = config['loginurl']
	self.photopath 	  = config['photopath']
	self.cmisurl      = config['cmisurl']
	self.ftpurl       = config['ftpurl']
	self.ftpport      = config['ftpport']
	self.imap_host 	  = config['imap_host']
	self.imap_port    = config['imap_port']
	self.addons 	  = config['addons']
		
	return self

def setBrowser(self):
	if self.testbrowser == 'firefox':
                return webdriver.Firefox()
        if self.testbrowser == 'chrome':
                return webdriver.Chrome()

