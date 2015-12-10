from yarn.api import env, cd, run
import private
import unittest

# pip3 install requests
import requests

def install(appName):
    result = run( "echo \'" + sudo + "\' | sudo -kS apt-get -q -y --force-yes install " + appName + " 2>&1")
    for line in result.lower().splitlines():
        if (line.startswith("e:")):
            print(result)
            exit()
    print ("Installed: " + appName)

def install_reqs():
    # install pyhton3
    if (not run("which python3")):
        install("python3")

    # install pip3
    if (not run("which pip3")):
        install("python3-pip")

    # install django 1.8
    if (not run("pip3 list | grep -io django")):
        result = run( "echo \'" + sudo + "\' | sudo -kS pip3 install django==1.8.4")
        print("Installed: Django")

    # install wget
    if (not run("which wget")):
        install("wget")

def app_setup():
    # download app and make root directory
    if (not run("ls -l | grep " + private.webRoot)):
        run("wget https://github.com/dtg3/st-site/archive/master.zip -O webapp.zip 2>&1")
        run("mkdir " + private.webRoot)

    # unzip app and cleanup zip file
    if (not run("ls -l " + private.webRoot + " | grep " + private.appRoot)):
        run("unzip webapp.zip -d " + private.webRoot + "/" + private.appRoot)
        run ("rm webapp.zip")
    
    # rename application directory
    if (not run("cd " + private.webRoot + "/" + private.appRoot + "; ls -l | grep " + private.appContent)):
        run("cd " + private.webRoot + "/" + private.appRoot + "; mv st-site-master " + private.appContent)

    # create database directory
    if (not run("cd " + private.webRoot + "/" + private.appRoot + "; ls -l | grep " + private.appDatabase)):
        run("cd " + private.webRoot + "/" + private.appRoot + "; mkdir " + private.appDatabase)
    
    # run databse migration
    if (not run("cd " + private.webRoot + "/" + private.appRoot + "/" + private.appDatabase + "; ls -l | grep db.sqlite3")):
        run("python3 " + private.webRoot + "/" + private.appRoot + "/" + private.appContent + "/manage.py migrate --noinput")

def app_start():
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
        run("nohup python3 " + private.webRoot + "/" + private.appRoot + "/" + private.appContent + "/manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1 &")

def app_stop():
    results = run("ps -ef")

    for line in results.splitlines():
        if (private.webRoot + "/" + private.appRoot + "/" + private.appContent + "/manage.py") in line.lower():
            run("kill -9 " + line.split()[1])

def config():
    env.host_string = private.host
    env.user = private.username
    env.password = private.password

    print("Install Requirements")
    install_reqs()
    print("Install App")
    app_setup()
    print("Launch App")
    app_start()
    print("Terminate App")
    app_stop()


if __name__ == "__main__":
    config()
