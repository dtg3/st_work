import setup
import enviro
import unit
import functional
import time
import requests
import unittest
import private
from yarn.api import env, cd, run

def start_server():
    print("Check Server Running...")
    started = False
    results = run("ps -ef")

    for line in results.splitlines():
        if (private.webRoot + "/" + private.appRoot + "/" + private.appContent + "/manage.py") in line.lower():
            started = True
    try:
        response = requests.get("http://" + private.host + ":" + private.port)
        if response.status_code == 200:
            started = True
    except requests.exceptions.RequestException as e:
        started = False


    if not started:
        print("Starting Server...")
        run("nohup python3 " + private.webRoot + "/" + private.appRoot + "/" + private.appContent + "/manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1 &")

def stop_server():
    results = run("ps -ef")

    for line in results.splitlines():
        if (private.webRoot + "/" + private.appRoot + "/" + private.appContent + "/manage.py") in line.lower():
            print("kill server pid: " + str(line.split()[1]) + "...")
            run("kill -9 " + line.split()[1])

def cleanup_db():
    run("python3 " + private.webRoot + "/" + private.appRoot + "/" + private.appContent + "/manage.py migrate --noinput")


# Environment Tests
class Test_000_Environ_PreReqs(enviro.Test_000_Environment):
    pass
class Test_001_Environ_AppInstall(enviro.Test_001_AppInstall):
    pass
class Test_002_Environ_RunningApp(enviro.Test_002_RunningApp):
    pass

# Unit Tests
class Test_003_UnitTests(unit.Test_000_AppUnitTests):
    pass

class Test_004_Functional(functional.NewVisitorTest):
    pass

if __name__ == "__main__":
    env.host_string = private.host
    env.user = private.username
    env.password = private.password

    # Config
    setup.config()

    start_server()
    time.sleep(5)

    # Run Test Suite
    unittest.main(exit=False, warnings='ignore')

    stop_server()
    cleanup_db()
