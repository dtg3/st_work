from yarn.api import env, cd, run
from private import host, username, password

import unittest

class Test_000_Utils(unittest.TestCase):
    def setUp(self):
        env.host_string = host
        env.user = username
        env.password = password

    def test_000_tmux(self):
        self.assertTrue(run("which tmux"))

if __name__ == "__main__":
    unittest.main()
