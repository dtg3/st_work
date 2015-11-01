from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import nypl_utility as utils

class NYPLResponsive(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(utils.nypl_new_catalog)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test001_searchbar_in_bounds_after_resize(self):
        # set new window size to mobile device size
        prev_size = self.browser.get_window_size()
        nww, nwh = 500, 560
        self.browser.set_window_size(nww, nwh)

        # get new search bar width, height, x, y after resize
        search_bar = self.browser.find_element_by_id("searchString")
        nsw, nsh = search_bar.size['width'], search_bar.size['height']
        nsx, nsy = search_bar.location['x'], search_bar.location['y']

        assert(nsw + nsx <= nww)
        assert(nsh + nsy <= nwh)

        # reset to original size
        self.browser.set_window_size(prev_size['width'], prev_size['height'])


if __name__ == '__main__':
    unittest.main(warnings='ignore')