from yarn.api import env, cd, run
from private import host, username, password

import unittest

class Test_000_Environment(unittest.TestCase):
    def setUp(self):
        env.host_string = host
        env.user = username
        env.password = password

    def test_000_tmux(self):
        self.assertTrue(run("which tmux"))

    def test_001_python3(self):
        self.assertTrue(run("which python3"))

    def test_002_pip3(self):
        self.assertTrue(run("which pip3"))

if __name__ == "__main__":
    unittest.main()
