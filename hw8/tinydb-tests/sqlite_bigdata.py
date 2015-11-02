import time
import sqlite3
import json
import unittest

f = open('sqlite_big_op_timing.csv', 'w')
f.write("op, time\n")
conn = sqlite3.connect('artifacts/sqlite_bigdata.db')
db = conn.cursor()

class SqliteBigData(unittest.TestCase):

	def setUp(self):
		cust_id = "123"
		cust_name = "Stark Industries"
		order_id = "abc"
		order_date = "2014-05-08"
		item_id = "a1b2c3"
		item_name = "Armor"
		item_qty = "8"
		item_cost = "$12345"

		db.execute("insert into orders(cust_id, cust_name, order_id, order_date, item_id, item_name, item_qty, item_cost) values (?, ?, ?, ?, ?, ?, ?, ?)", (cust_id, cust_name, order_id, order_date, item_id, item_name, item_qty, item_cost))

		conn.commit()

	def tearDown(self):
		db.execute('''delete from orders
			where cust_id = '123'
			and order_id = 'abc'
			and item_id = 'a1b2c3'
			''')
		conn.commit()


	def test_sqlite_01_bigdata_insert_record(self):
		print ("\nSQLITE BIG DATA --- INSERT RECORD")
		self.tearDown()

		cust_id = "123"
		cust_name = "Stark Industries"
		order_id = "abc"
		order_date = "2014-05-08"
		item_id = "a1b2c3"
		item_name = "Armor"
		item_qty = "8"
		item_cost = "$12345"

		t = time.time()
		db.execute("insert into orders(cust_id, cust_name, order_id, order_date, item_id, item_name, item_qty, item_cost) values (?, ?, ?, ?, ?, ?, ?, ?)", (cust_id, cust_name, order_id, order_date, item_id, item_name, item_qty, item_cost))

		conn.commit()
		t = time.time() - t
		f.write("insert record, " + str(t) + "\n")

		cursor = conn.execute('''
			SELECT * from orders
			where cust_id = '123'
			''')
		
		for row in cursor:
			self.assertTrue((row[0] == '123' and row[4] == 'a1b2c3'))

	
	def test_sqlite_02_bigdata_update_record(self):
		print ("\nSQLITE BIG DATA --- UPDATE RECORD")
		cursor = conn.execute('''
			SELECT * from orders
			where cust_id = '123'
			''')
		
		for row in cursor:
			self.assertTrue((row[2] == 'abc' and row[6] == 8))

		t = time.time()
		db.execute('''update orders set item_qty = 10 
			where cust_id = '123'
			and order_id = 'abc'
			and item_id = 'a1b2c3'
			''')
		conn.commit()
		t = time.time() - t
		f.write("update record, " + str(t) + "\n")

		cursor = conn.execute('''
			SELECT * from orders
			where cust_id = '123'
			''')
		
		for row in cursor:
			self.assertTrue((row[2] == 'abc' and row[6] == 10))


	def test_sqlite_03_bigdata_remove_record(self):
		print ("\nSQLITE BIG DATA --- REMOVE RECORD")
		cust_id = "0000000"
		cust_name = "Wayne Enterprises"
		order_id = "AAAAAA"
		order_date = "2015-05-05"
		item_id = "000111222"
		item_name = "Batmobile"
		item_qty = "1"
		item_cost = "$123456789"

		t = time.time()
		db.execute("insert into orders(cust_id, cust_name, order_id, order_date, item_id, item_name, item_qty, item_cost) values (?, ?, ?, ?, ?, ?, ?, ?)", (cust_id, cust_name, order_id, order_date, item_id, item_name, item_qty, item_cost))

		cursor = conn.execute('''
			SELECT * from orders
			where cust_id = '0000000'
			''')
		
		for row in cursor:
			self.assertTrue((row[2] == 'AAAAAA' and row[5] == 'Batmobile'))

		t = time.time()
		db.execute('''delete from orders
			where cust_id = '0000000'
			and order_id = 'AAAAAA'
			and item_id = '000111222'
			''')
		conn.commit()
		t = time.time() - t
		f.write("delete record, " + str(t) + "\n")

		cursor = conn.execute('''
			SELECT count(*) from orders
			where cust_id = '0000000'
			and order_id = 'AAAAAA'
			and item_id = '000111222'
			''')

		for row in cursor:
			for count in row:
				self.assertEqual(count, 0)
		

if __name__ == '__main__':
	unittest.main(warnings='ignore')
