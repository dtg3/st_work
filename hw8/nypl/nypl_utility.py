from selenium import webdriver
from selenium.webdriver.common.keys import Keys

nypl_new_catalog = "http://browse.nypl.org"
nypl_old_catalog = "http://catalog.nypl.org"

def search_new_catalog_by_keyword(browser, keyword):
	search_bar = browser.find_element_by_id("searchString")
	search_bar.send_keys(keyword)
	search_bar.send_keys(Keys.ENTER)
	browser.implicitly_wait(5)

