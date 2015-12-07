from yarn.api import env, cd, run
from private import host, username, password, sudo

import unittest

def install(appName):
    result = run( "echo \'" + sudo + "\' | sudo -kS apt-get -q -y --force-yes install " + appName + " 2>&1")
    for line in result.lower().splitlines():
        if (line.startswith("e:")):
            print(result)
            exit()
    print ("Installed: " + appName)

def install_reqs():
    # install tmux
    if (not run("which tmux")):
        install("tmux")

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
    if (not run("ls -l | grep webapps")):
        run("wget https://github.com/dtg3/st-site/archive/master.zip -O webapp.zip 2>&1")
        run("mkdir webapps")

    # unzip app and cleanup zip file
    if (not run("ls -l webapps | grep todo")):
        run("unzip webapp.zip -d webapps/todo")
        run ("rm webapp.zip")
    
    # rename application directory
    if (not run("cd webapps/todo; ls -l | grep superlists")):
        run("cd webapps/todo; mv st-site-master superlists")

    # create database directory
    if (not run("cd webapps/todo ls -l | grep database")):
        run("cd webapps/todo; mkdir database")
    
    # run databse migration
    if (not run("cd webapps/todo/database; ls -l | grep db.sqlite3")):
        run("cd webapps/todo/superlists; python3 manage.py migrate --noinput")
        #run("cd webapps/todo/superlists; python manage.py runserver 0.0.0.0:8000")

if __name__ == "__main__":
    env.host_string = host
    env.user = username
    env.password = password

    print("Install Requirements")
    install_reqs()
    print("Install App")
    app_setup()
