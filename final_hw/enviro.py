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

    def test_003_django(self):
        results = run("pip3 list | grep -io django.*")
        self.assertTrue(results)
        self.assertTrue("1.8" in results)

    def test_004_wget(self):
        self.assertTrue(run("which wget"))

class Test_001_AppInstall(unittest.TestCase):
    def setUp(self):
        env.host_string = host
        env.user = username
        env.password = password

    def test_000_app_directories(self):
        self.assertTrue(run("ls -l | grep webapps"))
        self.assertTrue(run("cd webapps; ls -l | grep todo"))
        self.assertTrue(run("cd webapps/todo; ls -l | grep superlists"))
        self.assertTrue(run("cd webapps/todo/; ls -l | grep database"))
        self.assertTrue(run("cd webapps/todo/database; ls -l | grep db.sqlite3"))
'''
class Test_002_LaunchApp(unittest.TestCase):
    def setUp(self):
        env.host_string = host
        env.user = username
        env.password = password

    def test_000_launch_app(self):
        results = run("tmux list-sessions 2>&1")        
        self.assertFalse("failed to connect to server: Connection refused" in results)
'''
if __name__ == "__main__":
    unittest.main()
