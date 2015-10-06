import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
	The Fox executives would like to check and see if their show
	"Brooklyn Nine Nine" is receiving postive reviews online. They
	will check to make sure that the site is reviewed well on Hulu
	with at least a rating higher than 3.5 stars out of 5. They also want to
	ensure that only the latest 5 episodes at most are available for
	free on the site. Additionally they will look at IMDb to see if
	the show is reviewed well there as well with a rating of 7 or
	higher out of 10.
'''

# Visit Google and search for Hulu
browser = webdriver.Firefox()
browser.get("http://www.google.com")
assert "Google" in browser.title
elem = browser.find_element_by_name("q")
elem.send_keys("hulu")
elem.send_keys(Keys.RETURN)

# Find the Hulu link and click it
time.sleep(2)
browser.find_element_by_xpath("//a[text()[contains(.,'Hulu:')]]").click()


# Search Hulu for Brooklyn Nine Nine
time.sleep(2)
assert "Hulu" in browser.title
hulu_search = browser.find_element_by_name("q")
hulu_search.send_keys("brooklyn nine nine")
hulu_search.send_keys(Keys.RETURN)


# Find the rating for the Brooklyn Nine Nine Show
time.sleep(2)
stars = browser.find_elements_by_xpath("//div[@class='promo-show-description']//span[@id='15137']/span")

rating = 0.0
for star in stars:
	# Count the full stars
	if ("full" in star.get_attribute("class")):
		rating = rating + 1
	# Count the half stars
	if ("half" in star.get_attribute("class")):
		rating = rating + 0.5

# Make sure the rating is higher than 3.5 stars
assert rating > 3.5

# Visit the Brooklyn Nine Nine Hulu page
browser.find_element_by_xpath("//a[@class='promo-title-link beacon-click']").click()

# Check that 5 or less episodes are currently free on Hulu
time.sleep(2)
assert int(browser.find_element_by_xpath("//div[@class='free-badge']/span").text) <= 5


# Visit IMDB
browser.get("http://www.imdb.com")
assert "IMDb" in browser.title

# Search IMDb for Brooklyn Nine Nine
time.sleep(2)
imdb = browser.find_element_by_name("q")
imdb.send_keys("brooklyn nine nine")
imdb.send_keys(Keys.RETURN)


# Check the rating of the Brooklyn Nine Nine show is greater than or equal to 7
time.sleep(2)
assert float(browser.find_element_by_xpath("//div[@class='titlePageSprite star-box-giga-star']").text) >= 7


time.sleep(5)
browser.close()
