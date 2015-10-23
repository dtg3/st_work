from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NYPLCatalogTest(unittest.TestCase):

    def setUp(self):
		options = webdriver.ChromeOptions()
		options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors","test-type"])
		options.add_argument("--start-maximized")
		options.add_argument('--disable-application-cache')
		self.browser = webdriver.Chrome(chrome_options=options)
		self.browser.implicitly_wait(3)

    def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main(warnings='ignore')
