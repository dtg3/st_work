from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import nypl_utility as utils

class NYPLSecure(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(utils.nypl_new_catalog)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')