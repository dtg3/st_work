# Homework B: Viability Testing for TinyDB
#### Drew Guarnera & Heather Michaud

The mission of the Viability Test is to asses the potential of using TinyDB
for the purposes of a small store customer database. We potentially have
1,000 customers, each of which may have 500 items that they have purchased.
One of the major fore-runners for database creation, manipulation, and
maintenance is the library that TinyDB provides.


### Requirements
In order to determine if TinyDB is viable for this purpose, we first define a
set of database actions which we wish to perform for the small store:
  - Add a customer
  - Add an item purchased to a customer's 'tab'
  - Add multiple instances of the same item purchased to the same customer
  - Delete a customer
  - Delete an item from a customer
  - View a customer and the items they have purchased
  - Determine which items are bought most frequently
  - Determine which items have been bought least frequently
  - Determine the type preference of a customer based on previous item choices

The addition, deletion, and viewing of the data for a particular customer or
item is crucial for any basic database operations. We expand further upon these
requirements by specifying that each of the following requirements must also be
met, provided a maximal database of 1000 customers, each with 500 items:
  - Add customer/item takes less than 0.05 seconds
  - Deleting a customer/item takes less than .1 seconds
  - Accessing a customer/item takes less than 0.01 seconds

We expect the most frequent operation that is performed is the accessing of
data within the database for frequently item set mining and other operations to
improve the customer experience, so fast access to the data is critical. As
we only expect to have 1,000 customers, additions to the database will be less
frequent though still relevant. Finally, the deletion of customers or items is
expected to happen least frequently so the performance for that is least
important.

We also want the API to be easy to use and clean. As this is subjective, we
define 'easy to use' such that the API has documentation and examples of each
operation we wish to perform. We define 'clean' such that basic operation (add,
view, delete) can be performed in one line of code.
