from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import nypl_utility as utils

class NYPLView(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(utils.nypl_new_catalog)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def t_can_get_isbn(self, isbn): 
        utils.search_new_catalog_by_keyword(self.browser, isbn)

         # we get one results
        titleDivs = self.browser.find_elements_by_class_name("dpBibTitle")
        self.assertTrue(len(titleDivs) > 0, "Could not retrieve any results based on isbn " + isbn)

        # result matches our expected title
        titleDivs[0].find_element_by_xpath("./span/a").click()
        self.browser.implicitly_wait(3)

        # that result has the ISBN we searched for
        additionalInfoDivs = self.browser.find_elements_by_class_name("bibInfoData")
        addInfo = []
        for item in additionalInfoDivs:
            addInfo.append(item.text)

        # we can view the isbn
        foundISBN = False
        for item in additionalInfoDivs:
            if isbn in item.text:
                foundISBN = True
        self.assertTrue(foundISBN, "Could not retrieve ISBN " + isbn + ".")


    def t_copies_match(self, isbn):
        self.browser.get(utils.nypl_new_catalog)
        self.browser.implicitly_wait(3)

        utils.search_new_catalog_by_keyword(self.browser, isbn)
        titleDivs = self.browser.find_elements_by_class_name("dpBibTitle")
        self.assertTrue(len(titleDivs) > 0, "Could not retrieve any results based on isbn " + isbn)

        # get book copies from new catalog
        titleDivs[0].find_element_by_xpath("./span/a").click()
        self.browser.implicitly_wait(3)
        expand = self.browser.find_elements_by_class_name("allRowItem")
        if len(expand) > 0:
            expand[0].click()
            self.browser.implicitly_wait(3)

        nCopies = self.browser.find_elements_by_xpath("//table[@class='itemTable']//tr")

        # search book by isbn in old catalog
        self.browser.get(utils.nypl_old_catalog)
        self.browser.implicitly_wait(3)

        self.browser.find_element_by_xpath("//select[@id='searchtype']/option[@value='i']").click()

        search_bar = self.browser.find_element_by_name("searcharg")
        search_bar.send_keys(isbn)
        search_bar.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)

        # book copies from old catalog
        expand = self.browser.find_elements_by_xpath("//input[@type='submit'][@value='View additional copies or search for a specific volume/copy']")
        if len(expand) > 0:
            expand[0].click()
            self.browser.implicitly_wait(3)
        oCopies = self.browser.find_elements_by_xpath("//div[@class='additionalCopies']/table//tr")

        # new catalog may have more resources (online) to pull copies from
        self.assertTrue(len(nCopies) >= len(oCopies))


    def DISABLED_test_001_view_isbn(self):
        self.t_can_get_isbn("0345391802")
        self.t_can_get_isbn("1451673310")
        self.t_can_get_isbn("0471043281")
        self.t_can_get_isbn("0811874559")


    def test_002_view_copies(self):
        self.t_copies_match("0345391802")
        self.t_copies_match("0553212478")


if __name__ == '__main__':
    unittest.main(warnings='ignore')
