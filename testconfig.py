from configure import Configuration
from selenium import webdriver

""" Collect params from config.yml """
def getVars(self):
	""" Used at setup of test """
	config = Configuration.from_file('./config.yml').configure()
		
	self.testbrowser  = config['browser']
	
	host = config['host']	
	port = config['port']		
	
	if config['https'] is True:
		uri = 'https'
	else:	
		uri = 'http'

	if port is None:
		self.url = uri + '://' + host 
	else:
		self.url = uri + '://' + host + ':' + port

	self.host	  = config['host']	
	self.username 	  = config['user']
	self.password 	  = config['passwd']
	self.loginurl  	  = self.url + config['loginurl']
	self.photopath 	  = config['photopath']
	self.cmisurl      = config['cmisurl']
	self.cmisatom 	  = self.url + config['cmisatom']
	self.ftpurl       = config['ftpurl']
	self.ftpport      = config['ftpport']
	self.imap_host 	  = config['imap_host']
	self.imap_port    = config['imap_port']
		
	return self

def setBrowser(self):
	if self.testbrowser == 'firefox':
                return webdriver.Firefox()
        if self.testbrowser == 'chrome':
                return webdriver.Chrome()
        if self.testbrowser == 'phantomjs':
                return webdriver.PhantomJS('/usr/local/bin/phantomjs')

