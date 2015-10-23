# Homework A: Acceptance Test Plan for NYPL Catalog
#### Drew Guarnera & Heather Michaud

The mission of the Acceptance Test is to provide stakeholders with information
about the quality of the New York Public Library (NYPL) Catalog, as found
on http://browse.nypl.org. This is determined by whether the product meets the
requirements as specified in the contract. Much of this is based on whether the
new catalog is consistent in functionality with the old catalog, as found on
http://catalog.nypl.org.

The value of the product is evaluated based on its value to the stakeholders,
who are assumed here to be the library (i.e., the people that paid for the
product). The software's customer is the library, but the library's customer is
the public. As a result, the library's interests are strongly aligned with the
public's in terms of functionality and usability, stability, performance, and
security.

### Requirements
There are many points of possible failure in the new product. The most basic
expected functionality, which is largely based on the old catalog, is as
follows:
  - Searching for a specific book based on
    * keyword
    * author
    * title
    * subject
    * genre
    * call number
    * category
    * ISBN
    * language
    * location of the specific library
  - Find books that can be found on the old catalog
  - View more information about a book
  - Check how many copies are available
  - Find the location where a copy is available

Additionally, the new features that have been introduced will be tested
to evaluate that they work as expected. This involves testing the responsive
design, such that:
  - When the browser is resized, the content follows
  - The search bar does not go outside of the boundaries of the page

Finally, the new catalog will be tested that it is secure against user
attack. This includes:
  - SQL injection
  - Non-ASCII characters
  - Maximum values (incredibly long search)
  - Minimum values (empty search)
  - Using HTML in the search


### Test plan & methodology
We narrow down this list to a set of 10 functional and non-functional tests.
The most commonly used functionality involves searching and viewing a specific
book, so these features are extensively tested. The non-functional set of tests
assures that the software is durable and reliable, including protection against
attack and verifying the responsiveness of the site.
  1. Search via keyword
  1. Search via title
  1. Search via ISBN
  1. Search via location
  1. View the ISBN of a book
  1. View number of copies for a book
  1. View location of a copy
  1. Searching with non-ASCII characters is allowable
  1. An SQL injection fails
  1. The search bar does not go outside of the boundaries of the page

The reason for the search selections is based on the assumption that the
majority of searches are from the user searching for a specific book by keyword,
its title, or specifically by ISBN. Additionally, because the NYPL has
multiple locations, a search by location is also crucial. Being able to view
the ISBN, the number of copies, and the location of that copy is also critical
for the user to be able to find a specific book that was searched for. As
multiple languages are supported within the library catalog, we must verify
that non-ASCII characters are supported. We verify that SQL injections fail
to prevent the entire database of the library catalog from being destroyed.
Lastly, as part of the contract for the new design called for a responsive,
resizable site. This will be tested via resizing the browser and testing that
the search bar, the most important element in the catalog, is not outside of
the bounds of the browser.

Each test will be conducted within a python script that utilizes selenium
to manipulate and test the web browser contents. The contents and results
as shown in the new product are at times compared to results as found via
Amazon, when a specific ISBN for a book is known. Additionally, the contents
and results in the new product are compared to the content and results that
the old product produces. Thus, both the old product and Amazon's book results
are used as testing oracles.

### Prototype
Due to familiarity with selenium in terms of functional testing, the
selected prototype test was one of a non-fuctional test for responsiveness
in the design. Here, we test that the search bar is within the bounds of the
window when the window has been resized to be smaller.

```python
def test10_searchbar_in_bounds_after_resize(self):
    # shrink the new window size
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
```
