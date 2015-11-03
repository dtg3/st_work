# Homework A: NYPL Catalog Acceptance Test Conclusion
#### Drew Guarnera & Heather Michaud

The Acceptance Test is meant to provide the library (i.e., the stakeholders)
with information about the quality of the New York Public Library (NYPL)
Catalog, as found on http://browse.nypl.org. This is determined by whether the
product meets the requirements as specified in the contract. To verify that
these requirements have been met, a set of ten functional and non-functional
automated tests were constructed using Python and Selenium. These are now
described in detail.

##### Search via keyword

Four phrases, "Hitchhiker's Gude to the Galaxy", "Algorithms", "Software
Testing", and "Fahrenheit 451" were used as keywords to search in the NYPL
Catalog. We first check that any results were returned. Then we compare that
the results that the product found correspond to the oracle (here, the old
NYPL catalog) - that at least the same or a greater number of results are
returned by the product than by the oracle. Additionally, that every title
that the oracle returned when searching by that same keyword is also found
in the product.

##### Search via title

Four phrases, "Hitchhiker's Gude to the Galaxy", "Algorithms", "Software
Testing", and "Fahrenheit 451" were used to search by title in the product.
We first check that any results were returned. Then we verify that all books
found have the searched title phrase in them.

##### Search via ISBN

Four ISBNs (0345391802, 1451673310, 0471043281, 0811874559) corresponding
to The Hitchhiker's Guide to the Galaxy, Fahrenheit 451, The Art of Software
Testing, and All My Friends Are Dead are used. For each ISBN, Amazon is
search to acquire the corresponding title. Then the NYPL Catalog is searched
by the same ISBN and we verify that this title matches the oracle's given
title (here, Amazon).

##### Search via location

Four separate titles are searched based on four separate locations. In one, we
look for "Harry Potter" at Tompkins Square. Next, "Software Testing" at 115th
street, then "Hitchhiker's Guide to the Galaxy" at St. Agnes, and finally we
search for "Don Quixote" at the Harlem library. In each scenario, the results
of the search are compared to that of the oracle (here, the old NYPL catalog).
We verify that the number of copies at the location is the same in both the
product and the oracle.

##### View the ISBN of a book

Four ISBNs (0345391802, 1451673310, 0471043281, 0811874559) corresponding
to The Hitchhiker's Guide to the Galaxy, Fahrenheit 451, The Art of Software
Testing, and All My Friends Are Dead are used. For each, we perform a search
via ISBN to find the books. Next, we verify that the same ISBN can be found
in the additional information listed for the title.

##### View number of copies for a book

Two books, The Hitchhiker's Guide to the Galaxy and Frankenstein, with ISBN
0345391802 and 0553212478 respectively, are searched via ISBN in the product.
In the results section we note the number of copies - whether they are
available or unavailable. Next, we search the oracle (here, the old NYPL
catalog) via the same ISBN and note the number of copies. Finally we verify
that the number of copies provided by the oracle and the product are the same.

##### View location of a copy

Two books, The Hitchhiker's Guide to the Galaxy and Frankenstein, with ISBN
0345391802 and 0553212478 respectively, are searched via ISBN in the product.
We keep track of the location of each copy, and verify that it is consistent
with the location of each copy as listed in the oracle (here, the old NYPL
catalog).

##### Searching with non-ASCII characters is allowable

Two books written in non-ASCII characters are searched for and we verify that
each search returns results. One is the Art of War, with the title in Chinese
characters. The other is Crime and Punishment as the title is written in
Russian characters.

##### An SQL injection fails

Four SQL injections are used during a search by keyword and we verify that
either results appear or the page says that no results, in order to check that
the site does not crash or produce an error.

##### The search bar does not go outside of the boundaries of the page

We verify that the search bar stays within the bounds of the page when the
browser is resized to be smaller.


## Evaluation


A search by keyword using the product revealed that a search for certain books
had less results when compared to the old version of the NYPL Catalog used as
an oracle. Specifically this was the case when searching for "Hitchhiker's
Guide to the Galaxy".

A search by title (e.g., "Harry Potter") and location (e.g. "Tompkins Square")
returned less results in the product when compared to the old version of the
NYPL Catalog used as an oracle (25 vs. 30).

In testing the view of the location in which copies are at, when searching for
The Hitchhiker's Guide to the Galaxy via ISBN, we found that the old catalog
had a copy of it at the Ottendorfer Fiction library, but the new catalog had
all of the same location listings except this one.

Doing a search by ISBN in the new catalog unexpectedly showed more than one
result in some cases (see 1451673310 for Fahrenheit 451). To mitigate this
disparity during testing that books can be searched by ISBN, we checked that
the results were at least less than five. However, while this was not
explicitly stated in the requirements we test for, the issue remains that a
search by unique ISBN does not return a single unique title.

Unless otherwise stated, the remaining tests passed.


## Conclusion

A set of ten functional and non-functional requirements were tested using
python and selenium. These automated tests verified the listed requirements in
terms of search and view functionality, as well as security and responsiveness.
Several issues were found with the functional requirements that caused the
acceptance test to fail. As these issues were discovered using simple test
cases, we expect that they persist in other cases throughout the system.

Thus, we conclude that the NYPL Catalog is not complete. While the
responsiveness and security features are acceptable based on the terms of
the contract, part of the expected search and view functionality has failed.
