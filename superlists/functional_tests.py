from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# The Doctor's Tardis is acting up. He's decided to use an
		# 	online to-do app to keep track of all the things he needs
		# 	to make the necesary repairs

		# He visits the website for the app
		self.browser.get('http://localhost:8000')

		# He notices the the application title mentions to-do
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# The starting screen allows The Doctor it jump right in and make
		#	a new to-do item

		# He enters in "Replace space-time locator"

		# He hits enter, and the page updates showing:
		# 	"1: Replace space-time locator"

		# An empty text box remains on the page allowing for another to-do item
		# 	to be entered. The Doctor enters:
		#	"Repair Tardis console"

		# The page updates again, and now shows both items on the list

		# The Doctor is always busy saving the planet (or any planet), so he needs
		# 	to make sure that the site lets him save his list for later.
		#	Upon saving the list, a unique URL is generated for him along with some
		# 	explanatory text to that effect

		# The Doctor visits the URL and makes sure that the list appears

if __name__ == '__main__':
    unittest.main(warnings='ignore')
