from yarn.api import env, cd, run
import private
import unittest
#import urllib.request
#import urllib.parse
#import urllib.error


class Test_000_Environment(unittest.TestCase):
    def setUp(self):
        env.host_string = private.host
        env.user = private.username
        env.password = private.password

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
        env.host_string = private.host
        env.user = private.username
        env.password = private.password

    def test_000_app_directories(self):
        self.assertTrue(run("ls -l | grep " + private.webRoot))
        self.assertTrue(run("cd " + private.webRoot + "; ls -l | grep " + private.appRoot))
        self.assertTrue(run("cd " + private.webRoot + "/" + private.appRoot + "; ls -l | grep " + private.appContent))
        self.assertTrue(run("cd " + private.webRoot + "/" + private.appRoot + "; ls -l | grep " + private.appDatabase))
        self.assertTrue(run("cd " + private.webRoot + "/" + private.appRoot + "/" + private.appDatabase + "; ls -l | grep db.sqlite3"))

class Test_002_LaunchApp(unittest.TestCase):
    def setUp(self):
        env.host_string = private.host
        env.user = private.username
        env.password = private.password

    def test_000_app_process(self):
        started = False
        results = run("ps -ef")

        for line in results.splitlines():

            if (private.webRoot + "/" + private.appRoot + "/" + private.appContent + "/manage.py") in line.lower():
                started = True

        self.assertTrue(started)

    #def test_001_request(self):
    #    req = urllib.request.Request("http://" + private.host + ":" + private.port)
    #    print(req)

if __name__ == "__main__":
    unittest.main()
