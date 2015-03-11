# alfresco-tests

Python Selenium Tests

So providing everything is installed, see install.sh.  Running the tests will create a folder named 'images', with screenshots for each test run, named with the function name calling it.  So identifying which tests dont appear as expected should be easier.  The tests currently check for expected titles, so if the title of the page is as expected, but the page does appear correctly, the test would still pass.  Adding additional checks can be added as required.  

Page_* holds the PageObject functions for the test suite.  These are included by the addons test_* file

Locators.py holds global variables and can be referenced by the functions in the addons page_* file. The test_* file holds the addons test suite, allowing addons to have their own independent test runs, as needed, which can easily be run from runtests.sh. 

config.yml (Configuration) test parameters.  

photopath : this holds the path to where screen shots will be stored.  Default images in the alfresco-test folder.  To disable screenshots set this path to ''

Current Test Coverage

11 test_share (alfresco share urls)

14 test_rm (records management)

02 test_jsconsole (JSConsole Addon)

01 test_services (FTP/CMIS)

with Xvfb-run installed

launch ./runtests.sh to run headless

launch from command line, python <testname> to see test interactively


If you can help with creating new tests please fork and provide us a pull request.  We are aiming to help <a href="http://www.orderofthebee.org">OOTB</a> with a reliable test suite, so any help is gratefully received
