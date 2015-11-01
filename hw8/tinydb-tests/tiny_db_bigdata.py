import time
from tinydb import TinyDB, where
import json
import unittest

db = TinyDB("bigdata.json")

class TinyDBBigDataTiming(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_tinydb_bigdata_add_customer(self):
        self.assertEqual(db.count(where('cust_id') == '3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9'), 0)
        t = time.time()

        db.insert(
        {"cust_id": "3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9",
        "cust_name": "Fuelworks",
        "orders": [
        {"order_id": "d8a40a2b-facc-4d0a-8b0f-32a4e9d7080c",
        "order_date": "2014-05-08",
        "items": [
        {"item_id": "aaaaaaaa-bbbb-cccc-dddd-1234567890ab",
        "item_name": "tablet",
        "item_qty": 1,
        "item_cost": "$100.00"},
        {"item_id": "fce48268-0b4c-4fba-994f-03174ab9c9a0",
        "item_name": "dolor",
        "item_qty": 80,
        "item_cost": "$129.78"},
        {"item_id": "5c5cbb74-1a91-4e11-ad5e-9b92cd0e9142",
        "item_name": "consectetur",
        "item_qty": 87,
        "item_cost": "$156.82"}]},
        {"order_id": "87d66f89-bff7-4d18-900d-a8410cc42a1b",
        "order_date": "2015-10-13",
        "items": [
        {"item_id": "4af5e7e1-6078-406b-aae8-3968b9455f9d",
        "item_name": "eiusmod",
        "item_qty": 82,
        "item_cost": "$50.35"},
        {"item_id": "ff18ea2a-9f4e-4381-8773-a7f1de8fcbbe",
        "item_name": "ea",
        "item_qty": 89,
        "item_cost": "$134.87"}]}]})
        
        t = time.time() - t
        self.assertEqual(db.count(where('cust_id') == '3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9'), 1)
        print("Add 1001st Customer: " + str(t))

    def test_tinydb_bigdata_add_item(self):
        #Check that order exists
        self.assertEqual(db.count(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c')), 1)

        # Find record and element number
        result = db.search(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c'))
        
        #Check that item doesn't already exist
        #TODO
    
        # Find record and element number
        result = db.search(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c'))
        element = db.get(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c'))
        
        # Add new item to the first order
        result[0]['orders'][0]['items'].append(
            {"item_id": "aaaaaaaa-bbbb-cccc-dddd-1234567890ab",
            "item_name": "tablet",
            "item_qty": 1,
            "item_cost": "$100.00"})

        # Update the database
        db.update(result[0], eids=[element.eid])

        # Debugs
        print (result[0]['orders'][0]['items'])
        print (element.eid)
        print(db.search(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c')))


    def test_tinydb_bigdata_remove_customer(self):
        self.assertEqual(db.count(where('cust_id') == '3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9'), 1)
        t = time.time()

        element = db.get(where('cust_id') == '3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9')
        db.remove(eids=[element.eid])

        t = time.time() - t
        self.assertEqual(db.count(where('cust_id') == '3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9'), 0)
        print("Remove 1001st Customer: " + str(t))


if __name__ == '__main__':
    unittest.main(warnings='ignore')
