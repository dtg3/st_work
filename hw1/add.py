def add(x,y):
    return x+y

import unittest

class Test_001_OtherAddFunction(unittest.TestCase):

    def test_simple_add(self):
        print("case 1")
        self.assertEqual(add(1,2),3)

    def test_negatives(self):
        self.assertEqual(add(-1,-2),-3)

class Test_002_AddFunction(unittest.TestCase):

    def test_000_simple_add(self):
        print("case 2A")
        self.assertEqual(add(1,2),3)

    def test_001_negatives(self):
        print("case 2B")
        self.assertEqual(add(-1,-2),-3)

if __name__ == "__main__":
    unittest.main()
