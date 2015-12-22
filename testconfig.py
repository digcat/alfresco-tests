from configure import Configuration
from selenium import webdriver

""" Collect params from config.yml """
def getVars(self):
    """ Used at setup of test """
    config = Configuration.from_file('./config.yml').configure()

    self.testbrowser  = config['browser']
    self.host = config['sharehost']	
    self.port = config['shareport']		
    self.sharehost = config['sharehost']
    self.shareport = config['shareport']
    self.repohost  = config['repohost']
    self.repoport  = config['repoport']
    self.host	     = config['sharehost']	

    if config['https'] is True:
       uri = 'https'
    else:	
       uri = 'http'

    if self.shareport is None:
       self.url = uri + '://' + self.sharehost 
    else:
       self.url = uri + '://' + self.sharehost + ':' + str(self.shareport)

    if self.repoport is None:
   		 self.repourl = uri + '://' + self.repohost
    else:
       self.repourl = uri + '://' + self.repohost + ':' + str(self.repoport)

    self.username  = config['user']
    self.password  = config['passwd']
    self.loginurl  = self.url + config['loginurl']
    self.photopath = config['photopath']
    self.cmisurl   = config['cmisurl']
    self.cmisatom  = self.repourl + config['cmisatom']
    self.ftpurl    = config['sharehost']
    self.ftpport   = config['ftpport']
    self.imap_host = config['imap_host']
    self.imap_port = config['imap_port']

    print self.repourl
    return self

def setBrowser(self):
    if self.testbrowser == 'firefox':
                return webdriver.Firefox()
    if self.testbrowser == 'chrome':
                return webdriver.Chrome()
    if self.testbrowser == 'phantomjs':
                return webdriver.PhantomJS('/usr/local/bin/phantomjs')
