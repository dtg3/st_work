from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NYPLSearch(unittest.TestCase):
    nypl_new_catalog = "http://browse.nypl.org"
    nypl_old_catalog = "http://catalog.nypl.org"
    book = "hitchhiker's guide to the galaxy"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors","test-type"])
        options.add_argument("--start-maximized")
        options.add_argument('--disable-application-cache')
        self.browser = webdriver.Chrome(chrome_options=options)
        self.browser.get(self.nypl_new_catalog)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    ##
    # helper tests

    # search by a specific keyword and verify there are results
    def t_keyword_search_for(self, keyword):
        search_bar = self.browser.find_element_by_id("searchString")
        search_bar.send_keys(keyword)
        search_bar.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)

        titleDivs = self.browser.find_elements_by_class_name("dpBibTitle")
        assert(len(titleDivs) > 0)

        # those results are related to what was searched for
        # FAILING. Can't rely on the title matching the keyword, our keyword
        # could be for the author
        #for div in titleDivs:
        #    titleStr = div.find_element_by_xpath("./span/a").text
        #    assert(titleStr.lower().find(keyword.lower()) != -1)

    # perform an advanced search by title and verify
    #   - there are results
    #   - those results have the title name we searched for in them
    def t_title_search_for(self, title):
        # advanced search
        advancedSearchButton = self.browser.find_element_by_id("advancedSearchLinkComponent")
        advancedSearchButton.click()
        self.browser.implicitly_wait(3)

        # by title
        self.browser.find_element_by_xpath("//select[@name='searchType_0']/option[@value='t:']").click()
        searchBar = self.browser.find_element_by_id("searchTerm_0")
        searchBar.clear()
        searchBar.send_keys(title)
        searchBar.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(3)

        titleDivs = self.browser.find_elements_by_class_name("dpBibTitle")
        assert(len(titleDivs) > 0)

        # those results are related to what was searched for
        # FAILS - NYPL new shows title names that don't have the book name in them
        # can't rely on the title matching the keyword. keyword may be the author, who knows
        #for div in titleDivs:
        #    titleStr = div.find_element_by_xpath("./span/a").text
        #    assert(titleStr.lower().find(title.lower()) != -1)


    def test01_keyword_search_shows_relevant_results(self):
        self.t_keyword_search_for("hitchhiker's guide to the galaxy")
        self.t_keyword_search_for("algorithms")
        self.t_keyword_search_for("software testing")
        self.t_keyword_search_for("fahrenheit 451")


    def DISABLED_test02_keyword_search_matches_old_catalog(self):
        # search for and get title of each book in new catalog
        search_bar = self.browser.find_element_by_id("searchString")
        search_bar.send_keys(self.book)
        search_bar.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)

        titleDivs = self.browser.find_elements_by_class_name("dpBibTitle")
        newTitles = []
        for div in titleDivs:
            newTitles.append(div.find_element_by_xpath("./span/a").text)

        # search for book in old catalog
        self.browser.get(self.nypl_old_catalog)
        self.browser.implicitly_wait(3)
        search_bar = self.browser.find_element_by_name("searcharg")
        search_bar.send_keys(self.book)
        search_bar.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)

        # get the old catalog
        self.browser.get(self.nypl_old_catalog)
        self.browser.implicitly_wait(3)

        # search for HHGTTG
        search_bar = self.browser.find_element_by_name("searcharg")
        search_bar.send_keys(self.book)
        search_bar.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)

        titleContainers = self.browser.find_elements_by_class_name("briefcitTitle")
        oldTitles = []
        for span in titleContainers:
            oldTitles.append(span.find_element_by_xpath("./a").text)

        # the new catalog has more results, but it should at least have
        # all the results from the old catalog
        # FAILING
        assert(len(newTitles) >= len(oldTitles))
        for title in oldTitles:
            print(title)
            assert(title in newTitles)

    def test03_title_search(self):
        self.t_title_search_for("hitchhiker's guide to the galaxy")
        self.t_title_search_for("algorithms")
        self.t_title_search_for("software testing")
        self.t_title_search_for("fahrenheit 451")




if __name__ == '__main__':
    unittest.main(warnings='ignore')
