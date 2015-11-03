import time
from tinydb import TinyDB, where
import json
import unittest

db = TinyDB("data.json")
f = open('small_op_timing.csv', 'w')
f.write("op, time\n")

class TinyDBSmallData(unittest.TestCase):

    def setUp(self):
        db.insert( { 'customerid': 1, 'items': [ {'name': 'raspberry pi', 'price': 30}, {'name': 'pi case', 'price': 8} ] } )
        db.insert( { 'customerid': 3, 'items': [ {'name': 'laptop', 'price': 900}, {'name': 'mouse', 'price': 20} ] } )


    def tearDown(self):
        db.purge()


    def test_tinydb_01_add_record(self):
        print("\nSMALL DATA --- ADD RECORD")

        #Check if new record customer 2 doesn't exist
        self.assertEqual(db.count((where('customerid') == 2)), 0)

        #Insert record for customer 2
        t = time.time()
        db.insert( { 'customerid': 2, 'items': [ {'name': 'touch screen', 'price': 90}, {'name': 'bluetooth', 'price': 15} ] } )
        t = time.time() - t
        f.write('insert customer record, ' + str(t) + '\n')

        #Confirm customer 2 has been added
        self.assertEqual(db.count((where('customerid') == 2)), 1)


    def test_tinydb_02_add_item(self):
        print("\nSMALL DATA --- ADD ITEM")

        # Check that new item doesn't exist for customer 1
        self.assertEqual(db.count((where('customerid') == 1) & (where('items').any(where('name') == 'battery'))), 0)

        # Grab customer 1 data
        result = db.search(where('customerid') == 1)

        # Grab customer 1 element info
        element = db.get(where('customerid') == 1)

        # Insert a new item and save it
        t = time.time()
        result[0]['items'].append( {'name': 'battery', 'price': 1} )
        db.update(result[0], eids=[element.eid])
        t = time.time() - t
        f.write('insert item into customer, ' + str(t) + '\n')

        # Check that new item now exists
        self.assertEqual(db.count((where('customerid') == 1) & (where('items').any(where('name') == 'battery'))), 1)


    def test_tinydb_03_update_item(self):
        print("\nSMALL DATA --- UPDATE ITEM")

        self.assertEqual(db.count((where('customerid') == 3) & (where('items').any(where('name') == 'laptop'))), 1)

        # Grab customer 3 data
        result = db.search(where('customerid') == 3)
        # Grab customer 1 element info
        element = db.get(where('customerid') == 3)

        t = time.time()
        for item in result[0]['items']:
            if item['name'] == 'laptop':
                item['name'] = 'desktop'
                break

        db.update(result[0], eids=[element.eid])
        t = time.time() - t
        f.write('update item, ' + str(t) + '\n')

        self.assertEqual(db.count((where('customerid') == 3) & (where('items').any(where('name') == 'laptop'))), 0)
        self.assertEqual(db.count((where('customerid') == 3) & (where('items').any(where('name') == 'desktop'))), 1)


    def test_tinydb_04_remove_item(self):
        print("\nSMALL DATA --- REMOVE ITEM")

        self.assertEqual(db.count((where('customerid') == 1) & (where('items').any(where('name') == 'raspberry pi'))), 1)

        # Grab customer 3 data
        result = db.search(where('customerid') == 1)
        # Grab customer 1 element info
        element = db.get(where('customerid') == 1)

        t = time.time()
        itemIndex = 0
        for item in result[0]['items']:
            if item['name'] == 'raspberry pi':
                break
            itemIndex += 1

        del (result[0]['items'][itemIndex])

        db.update(result[0], eids=[element.eid])
        t = time.time() - t
        f.write('remove item, ' + str(t) + '\n')

        self.assertEqual(db.count((where('customerid') == 1) & (where('items').any(where('name') == 'raspberry pi'))), 0)

    def test_tinydb_05_remove_record(self):
        print("\nSMALL DATA --- REMOVE RECORD")

        self.assertEqual(db.count((where('customerid') == 1) & (where('items').any(where('name') == 'raspberry pi'))), 1)

        t = time.time()
        element = db.get(where('customerid') == 1)
        db.remove(eids=[element.eid])
        t = time.time() - t
        f.write('remove customer record, ' + str(t) + '\n')

        self.assertEqual(db.count((where('customerid') == 1)), 0)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
