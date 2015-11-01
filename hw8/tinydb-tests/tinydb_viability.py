import unittest
import tiny_db_smalldata
import tiny_db_bigdata

class Test_000_SmallData(tiny_db_smalldata.TinyDBSmallData):
	pass

class Test_001_BigData(tiny_db_bigdata.TinyDBBigData):
	pass

if __name__ == "__main__":
    unittest.main()
