import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Visit the Mariot Rewards Website
browser = webdriver.Firefox()
browser.get("http://www.marriott.com/rewards/rewards-program.mi")
assert "Marriott Hotel Rewards" in browser.title

# Click the "Find & Reserve" 
time.sleep(1)
browser.find_element_by_xpath("//a[@id='header-find-panel-trigger']").click()

# Click in the "Location" textbox
time.sleep(1)
browser.find_element_by_xpath("//input[@id='global-header-search-location']").click()

# Select the "Rewards number" textbox
time.sleep(1)
rewardsNumber = browser.find_element_by_xpath("//input[@name='marriottRewardsNumber']")

# Entering this sequence of characters as a rewards number causes an "Access Denied Page".
# If you remove or reorder any of these characters, regular input validation takes place.
rewardsNumber.send_keys(")(&")

time.sleep(5)
rewardsNumber.send_keys(Keys.RETURN)
time.sleep(10)
browser.close()
