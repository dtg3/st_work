from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import nypl_utility as utils

class NYPLView(unittest.TestCase):
    nypl_new_catalog = "http://browse.nypl.org"
    nypl_old_catalog = "http://catalog.nypl.org"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors","test-type"])
        options.add_argument("--start-maximized")
        options.add_argument('--disable-application-cache')
        self.browser = webdriver.Chrome(chrome_options=options)
        self.browser.get(self.nypl_new_catalog)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def t_can_get_isbn(self, isbn):
        utils.search_new_catalog_by_keyword(self.browser, isbn)

         # we get one results
        titleDivs = self.browser.find_elements_by_class_name("dpBibTitle")
        self.assertTrue(len(titleDivs) > 0, "Could not retrieve any results based on isbn " + isbn)

        # result matches our expected title
        titleDivs[0].find_element_by_xpath("./span/a").click()
        self.browser.implicitly_wait(3)

        # that result has the ISBN we searched for
        additionalInfoDivs = self.browser.find_elements_by_class_name("bibInfoData")
        addInfo = []
        for item in additionalInfoDivs:
            addInfo.append(item.text)

        # we can view the isbn
        foundISBN = False
        for item in additionalInfoDivs:
            if isbn in item.text:
                foundISBN = True
        self.assertTrue(foundISBN, "Could not retrieve ISBN " + isbn + ".")

    def test_001_view_isbn(self):
        self.t_can_get_isbn("0345391802")
        self.t_can_get_isbn("1451673310")
        self.t_can_get_isbn("0471043281")
        self.t_can_get_isbn("0811874559")



if __name__ == '__main__':
    unittest.main(warnings='ignore')
