import time
from tinydb import TinyDB, where
import json
import unittest

db = TinyDB("bigdatatiming.json")
f = open('big_timing.csv', 'w')

class TinyDBBigDataTiming(unittest.TestCase):

    def setUp(self):
        with open('artifacts/test_data.json') as data_file:
            data = json.load(data_file)
            f.write("rec#,insert_time\n")
            
            rec = 0
            t = 0

            for record in data:
                t = time.time()
                db.insert(record)
                t = time.time() - t
                f.write(str(rec) + ',' + str(t) + '\n')
                rec = rec + 1

    def tearDown(self):
        db.close()

    def test_tinydb_bigdata_timing(self):
        pass

if __name__ == '__main__':
    unittest.main(warnings='ignore')
