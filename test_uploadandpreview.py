import ftplib
import os
import unittest

import page
import testconfig

"""  testUploadAndPreviewMyAlfresco """


class testUploadAndPreviewMyAlfresco(unittest.TestCase):
    """testUploadAndPreviewMyAlfresco Class"""

    def setUp(self):
        """Setup browser and connection"""
        self = testconfig.getVars(self)
        self.driver = testconfig.setBrowser(self)
        self.driver.get(self.loginurl)

    def test_UploadAndPreview_alfresco_upload(self):
        import time

        main_page = page.MainPage(self.driver)
        main_page.click_login_button()
        sitename = "Alfresco-Hackathon"
        main_page.click_create_siteforpreviews(sitename)
        time.sleep(30)

    def test_UploadAndPreview_alfresco_ftp(self):
        sitename = "Alfresco-Hackathon"

        # SECURITY WARNING: Plain FTP transmits credentials and data in cleartext
        # Consider using FTP_TLS for encrypted transmission in production environments
        f = ftplib.FTP()
        f.connect(self.ftpurl, port=self.ftpport)
        f.login(self.username, self.password)
        destination = "/Alfresco/Sites/" + sitename + "/documentLibrary/"
        filestotest = []
        for root, _dirs, files in os.walk("previewtestfiles"):
            for fname in files:
                full_fname = os.path.join(root, fname)
                fulldestination = destination
                print(fulldestination)
                f.storbinary("STOR " + fulldestination + "/" + fname, open(full_fname, "rb"))
                filestotest.append("site/" + sitename + "/documentlibrary/" + fname)

        print(f.pwd())
        print(filestotest)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
