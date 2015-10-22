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
  1. The site is responsive