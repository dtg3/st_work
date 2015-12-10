from yarn.api import env, cd, run
import private
import unittest

class Test_000_AppUnitTests(unittest.TestCase):
    def setUp(self):
        env.host_string = private.host
        env.user = private.username
        env.password = private.password

    def test_000_unit_tests(self):
        result = run("python3 " + private.webRoot + "/" + private.appRoot + "/" + private.appContent + "/manage.py test lists &>/dev/null; echo $?")
        self.assertTrue(result == "0")

if __name__ == "__main__":
    unittest.main()
