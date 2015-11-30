from yarn.api import env, cd, run
import unittest

class Test_001_Applications(unittest.TestCase):
    
    def setUp(self):
        env.host_string = "********"
        env.user = "********"
        env.password = "********"

    def test_001_01_not_installed(self):
        print("\nCheck that emacs is NOT installed")
        self.assertFalse(run("which emacs"))
    
    def test_001_02_installed(self):
        print ("\nCheck that nano IS installed")
        self.assertTrue(run("which nano"))

    def test_001_03_default_application(self):
        print ("\nCheck which Python is default")

        which = run("which python")
        self.assertTrue(which == '/usr/bin/python')

        print(which)

    def test_001_04_installed_version(self):
        print ("\nCheck if Python3 version 3.4.X is installed")

        if run("which python3"):
            python_version = run("python3 --version")
            print (python_version)
            self.assertTrue("Python 3.4" in python_version)
        else:
            self.assertTrue(False)


class Test_002_Filesystem(unittest.TestCase):

    def setUp(self):
        env.host_string = "********"
        env.user = "********"
        env.password = "********"
        run("mkdir -p testdir; cd testdir; echo \"example file\" > sample.txt")
        
    def tearDown(self):
        run("rm -rf testdir")

    def test_002_01_directory_exists(self):
        print("\nCheck if directory exists")
        self.assertTrue("testdir" in run("find ~/ -type d -name \"testdir\""))

    def test_002_02_directory_missing(self):
        print("\nCheck if directory missing")
        self.assertTrue(run("find ~/ -type d -name \"missingdir\"") == "")

    def test_002_03_file_exists(self):
        print("\nCheck if file exists")
        self.assertTrue(run("test -f ~/testdir/sample.txt; echo $?") == "0")

    def test_002_04_file_missing(self):
        print("\nCheck if file missing")
        self.assertTrue(run("test -f ~/testdir/missing.txt; echo $?") == "1")

    def test_002_05_file_content(self):
        print("\nCheck if file contants word \"example\"")
        self.assertTrue("example" in run("cat ~/testdir/sample.txt"))

if __name__ == "__main__":
    unittest.main()
