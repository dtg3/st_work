from tinydb import TinyDB, where
import json
import unittest
import calc

class Test_000_TinyDB(unittest.TestCase):

    def test_insert_list_item(self):
        #Setup
        #db.purge()
        db.insert( {'items': [{'name': 'bacon'}, {'name': 'eggs'}]} )

        # get and print current state of database (could search for anything here)
        #f = db.all()
        #print(f)

        #get the first element in the list, at key followers. append to this list
        #f[0]['followers']
        #f[0]['followers'].append( {'name': 'heather'} )
        #print(f[0])

        #el = db.get(where('followers'))

        #print(el)
        #print(el.eid)

        # update using this new list, where the old list is (at eid = 1)
        #db.update(f[0], eids=[1] )
        #print( db.all() )

        db.purge()
        db.close()

if __name__ == "__main__":
    unittest.main()
