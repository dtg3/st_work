from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NYPLSearch(unittest.TestCase):
    nypl_new_catalog = "http://browse.nypl.org"
    npyl_old_catalog = "http://catalog.nypl.org"


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

    def test01_search_via_keyword(self):
        search_bar = self.browser.find_element_by_id("searchString")
        search_bar.send_keys("hitchhiker's guide to the galaxy")
        search_bar.send_keys(Keys.ENTER)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
