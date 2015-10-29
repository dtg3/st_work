import time
from tinydb import TinyDB, where
import json
import unittest

db = TinyDB("data.json")

class TinyDBAdd(unittest.TestCase):

    def setUp(self):
        db.insert( { 'customerid': 1, 'items': [ {'name': 'raspberry pi', 'price': 30}, {'name': 'pi case', 'price': 8} ] } )
        db.insert( { 'customerid': 2, 'items': [ {'name': 'touch screen', 'price': 90}, {'name': 'bluetooth', 'price': 15} ] } )

    def tearDown(self):
        db.purge()
        db.close()

    def test_tinydb_add_item(self):
        # Check that new item doesn't exist for customer 1
        self.assertEqual(db.count((where('customerid') == 1) & (where('items').any(where('name') == 'battery'))), 0)

        # Grab customer 1 data
        result = db.search(where('customerid') == 1)

        # Grab customer 1 element info
        element = db.get(where('customerid') == 1)

        # Insert a new item and save it
        result[0]['items'].append( {'name': 'battery', 'price': 1} )
        db.update(result[0], eids=[element.eid])

        # Check that new item now exists
        self.assertEqual(db.count((where('customerid') == 1) & (where('items').any(where('name') == 'battery'))), 1)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
