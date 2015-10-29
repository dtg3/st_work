import time
from tinydb import TinyDB, where
import json
import unittest

db = TinyDB("bigdata.json")

class TinyDBBigData(unittest.TestCase):

    def setUp(self):
        '''with open('test_data.json') as data_file:
            data = json.load(data_file)
            db.insert(data[0])
            print (db.all())'''
        db.purge()

    def tearDown(self):
        db.close()

    def test_tinydb_bigdata_search(self):
        pass



if __name__ == '__main__':
    unittest.main(warnings='ignore')
