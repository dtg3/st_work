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

	def test_can_search_with_nonascii_characters(self):
		# look for the art of war
		utils.search_new_catalog_by_keyword(self.browser, "孫子兵法")
		titleDivs = self.browser.find_elements_by_class_name("dpBibTitle")
		self.assertTrue(len(titleDivs) > 0,
            "Did not return any results when searching for the art of war in chinese")

		# look for crime and punishment
		utils.search_new_catalog_by_keyword(self.browser, "Преступление и наказание")
		titleDivs = self.browser.find_elements_by_class_name("dpBibTitle")
		self.assertTrue(len(titleDivs) > 0,
            "Did not return any results when searching for crime and punishment in russian")


if __name__ == '__main__':
	unittest.main(warnings='ignore')