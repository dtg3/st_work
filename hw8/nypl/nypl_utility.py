from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def search_new_catalog_by_keyword(browser, keyword):
	search_bar = browser.find_element_by_id("searchString")
	search_bar.send_keys(keyword)
	search_bar.send_keys(Keys.ENTER)
	browser.implicitly_wait(5)

