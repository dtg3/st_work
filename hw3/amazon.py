from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("http://www.amazon.com")
assert "Amazon" in browser.title
elem = browser.find_element_by_name("field-keywords")
elem.send_keys("coffee")
elem.send_keys(Keys.RETURN)
assert "coffee" in browser.page_source