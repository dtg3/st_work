import time
import sqlite3
import json
import unittest

f = open('sqlite_big_timing.csv', 'w')
conn = sqlite3.connect('sqlite_bigdata.db')
db = conn.cursor()

class SqliteInsertTiming(unittest.TestCase):

    def setUp(self):
        with open('artifacts/test_data.json') as data_file:
            data = json.load(data_file)
            f.write("rec#,insert_time\n")
            
            db.execute('''CREATE TABLE orders
                (cust_id text, cust_name text, order_id text, order_date date, item_id text, item_name text, item_qty real, item_cost real)''')

            conn.commit()

            rec = 0

            for record in data:
                cust_id = record['cust_id']
                cust_name = record['cust_name']
                for order in record['orders']:
                    order_id = order['order_id']
                    order_date = order['order_date']
                    for item in order['items']:
                        item_id = item['item_id']
                        item_name = item['item_name']
                        item_qty = item['item_qty']
                        item_cost = item['item_cost']
                        t = time.time()
                        db.execute("insert into orders(cust_id, cust_name, order_id, order_date, item_id, item_name, item_qty, item_cost) values (?, ?, ?, ?, ?, ?, ?, ?)", 
                            (cust_id, cust_name, order_id, order_date, item_id, item_name, item_qty, item_cost))
                        conn.commit()
                        t = time.time() - t
                        f.write(str(rec) + ',' + str(t) + '\n')
                        rec = rec + 1
                        print (rec)
        f.close()
        conn.close()

    def tearDown(self):
        db.close()

    def sqlite_bigdata_timing(self):
        pass

if __name__ == '__main__':
    unittest.main(warnings='ignore')
