import time
from tinydb import TinyDB, where
import json
import unittest

db = TinyDB("bigdata.json")

f = open('big_op_timing.csv', 'w')
f.write("op, time\n")

class TinyDBBigData(unittest.TestCase):

    def setUp(self):
        db.insert(
        {"cust_id": "3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9",
        "cust_name": "Fuelworks",
        "orders": [
        {"order_id": "d8a40a2b-facc-4d0a-8b0f-32a4e9d7080c",
        "order_date": "2014-05-08",
        "items": [
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


    def tearDown(self):
        if db.count(where('cust_id') == '3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9') == 1:
            element = db.get(where('cust_id') == '3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9')
            db.remove(eids=[element.eid])


    def test_tinydb_bigdata_01_add_customer(self):
        print ("\nADD CUSTOMER")
        self.tearDown()

        #verify customer doesn't exist
        self.assertEqual(db.count(where('cust_id') == '3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9'), 0)
        t = time.time()

        db.insert(
        {"cust_id": "3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9",
        "cust_name": "Fuelworks",
        "orders": [
        {"order_id": "d8a40a2b-facc-4d0a-8b0f-32a4e9d7080c",
        "order_date": "2014-05-08",
        "items": [
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
        f.write('insert customer record, ' + str(t) + '\n')


    def test_tinydb_bigdata_02_add_item(self):
        print ("\nADD ITEM")

        #Check that order exists
        self.assertEqual(db.count(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c')), 1)

        # Find record
        t = time.time()
        result = db.search(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c'))
        element = db.get(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c'))
        t = time.time() - t

        f.write('query record, ' + str(t) + '\n')

        #Check that item doesn't already exist
        orderIndex = 0
        found = False

        t = time.time()
        for order in result[0]['orders']:
            if order['order_id'] == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c':
                for item in order['items']:
                    if item['item_id'] == 'aaaaaaaa-bbbb-cccc-dddd-1234567890ab':
                        found = True
                        break
                break
            orderIndex+=1
        
        t = time.time() - t
        f.write('search in memory json (item in order), ' + str(t) + '\n')
        self.assertFalse(found)
        
        # Add new item to the first order
        t = time.time()
        result[0]['orders'][orderIndex]['items'].append(
            {"item_id": "aaaaaaaa-bbbb-cccc-dddd-1234567890ab",
            "item_name": "tablet",
            "item_qty": 1,
            "item_cost": "$100.00"})

        # Update the database
        db.update(result[0], eids=[element.eid])
        t = time.time() - t
        f.write('insert item into order, ' + str(t) + '\n')

        # Check the database to see if item now exists
        result = db.search(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c'))

        found = False

        for order in result[0]['orders']:
            if order['order_id'] == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c':
                for item in order['items']:
                    if item['item_id'] == 'aaaaaaaa-bbbb-cccc-dddd-1234567890ab':
                        found = True
                        break
                break
        
        self.assertTrue(found)


    def test_tinydb_bigdata_03_add_order(self):
        print ("\nADD ORDER")
        # Ensure order doesn't exist
        self.assertEqual(db.count(where('orders').any(where('order_id') == 'b371a85e-e955-430c-8653-aca6a040a5b5')), 0)
        
        # Ensure customer record to add item to does exist
        self.assertEqual(db.count(where('cust_id') == '3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9'), 1)

        t = time.time()
        result = db.search(where('cust_id') == '3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9')
        element = db.get(where('cust_id') == '3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9')

        result[0]['orders'].append(
        {"order_id": "b371a85e-e955-430c-8653-aca6a040a5b5",
        "order_date": "2014-01-06",
        "items": [
        {"item_id": "6e4573eb-17e2-418a-ba8b-437b624c70d5",
        "item_name": "computer",
        "item_qty": 99,
        "item_cost": "$144.72"},
        {"item_id": "264b9963-e982-4528-a8b3-f9e57cd6464f",
        "item_name": "consequat",
        "item_qty": 66,
        "item_cost": "$153.40"}]})

        db.update(result[0], eids=[element.eid])
        t = time.time() - t
        f.write('insert order to customer, ' + str(t) + '\n')

        # Ensure order now exists
        self.assertEqual(db.count(where('orders').any(where('order_id') == 'b371a85e-e955-430c-8653-aca6a040a5b5')), 1)


    def test_tinydb_bigdata_04_remove_item(self):
        print ("\nREMOVE ITEM")
        #Check that order exists
        self.assertEqual(db.count(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c')), 1)

        t = time.time()
        # Find record
        result = db.search(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c'))
        element = db.get(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c'))


        #Check find the item
        orderIndex = 0
        itemIndex = 0
        found = False

        for order in result[0]['orders']:
            if order['order_id'] == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c':
                for item in order['items']:
                    if item['item_id'] == 'fce48268-0b4c-4fba-994f-03174ab9c9a0':
                        found = True
                        break

                    itemIndex+=1
                break
            orderIndex+=1

        self.assertTrue(found)
        
        # Add new item to the first order
        del (result[0]['orders'][orderIndex]['items'][itemIndex])

        # Update the database
        db.update(result[0], eids=[element.eid])
        
        t = time.time() - t
        f.write('remove item from order, ' + str(t) + '\n')

        #Check the database to see if item now exists
        result = db.search(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c'))

        found = False

        for order in result[0]['orders']:
            if order['order_id'] == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c':
                for item in order['items']:
                    if item['item_id'] == 'fce48268-0b4c-4fba-994f-03174ab9c9a0':
                        found = True
                        break
                break
        
        self.assertFalse(found)


    def test_tinydb_bigdata_05_remove_order(self):
        print ("\nREMOVE ORDER")
        #Check that order exists
        self.assertEqual(db.count(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c')), 1)

        # Find record
        t = time.time()
        result = db.search(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c'))
        element = db.get(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c'))

        #Check find the item
        orderIndex = 0
        itemIndex = 0
        found = False

        for order in result[0]['orders']:
            if order['order_id'] == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c':
                break

            orderIndex+=1
        
        del (result[0]['orders'][orderIndex])
        db.update(result[0], eids=[element.eid])
        t = time.time() - t
        f.write('remove order from customer, ' + str(t) + '\n')

        #Check that order doesn't exist
        self.assertEqual(db.count(where('orders').any(where('order_id') == 'd8a40a2b-facc-4d0a-8b0f-32a4e9d7080c')), 0)


    def test_tinydb_bigdata_06_remove_customer(self):
        print ("\nREMOVE CUSTOMER")

        self.assertEqual(db.count(where('cust_id') == '3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9'), 1)
        t = time.time()

        element = db.get(where('cust_id') == '3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9')
        db.remove(eids=[element.eid])

        t = time.time() - t
        f.write('Remove customer record, ' + str(t) + '\n')
        self.assertEqual(db.count(where('cust_id') == '3ae8a9f7-0f54-498b-8e89-b8fe7e43a8a9'), 0)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
