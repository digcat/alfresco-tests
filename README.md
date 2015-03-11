# alfresco-tests

Python Selenium Tests

config.yml (Configuration) test parameters.  

photopath : this holds the path to where screen shots should be stored.  Default images in the alfresco-test folder.  To disable screenshots set this path to ''

Test Coverage

11 test_share (alfresco share urls)

14 test_rm (records management)

02 test_jsconsole (JSConsole Addon)

01 test_services (FTP/CMIS)

with Xvfb-run installed

launch ./runtests.sh to run headless

launch from command line, python <testname> to see test interactively


If you can help with creating new tests please fork and provide us a pull request.  We are aiming to help <a href="www.orderofthebee.org">OOTB</a> with a reliable test suite, so any help is gratefully received
