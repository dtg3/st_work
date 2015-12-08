from yarn.api import env, cd, run
from private import host, username, password

import unittest

class Test_000_Environment(unittest.TestCase):
    def setUp(self):
        env.host_string = host
        env.user = username
        env.password = password

    def test_000_python3(self):
        self.assertTrue(run("which python3"))

    def test_001_pip3(self):
        self.assertTrue(run("which pip3"))

    def test_002_django(self):
        results = run("pip3 list | grep -io django.*")
        self.assertTrue(results)
        self.assertTrue("1.8" in results)

    def test_003_wget(self):
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

class Test_002_LaunchApp(unittest.TestCase):
    def setUp(self):
        env.host_string = host
        env.user = username
        env.password = password

    def test_000_app_running(self):
        started = False
        results = run("ps -ef")

        for line in results.splitlines():
            if "webapps/todo/superlists/manage.py" in line.lower():
                started = True

        self.assertTrue(started)

if __name__ == "__main__":
    unittest.main()
