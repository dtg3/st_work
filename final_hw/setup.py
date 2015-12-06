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

def install_utils():
    # install tmux
    if (not run("which tmux")):
        install("tmux")

    if (not run("which python3")):
        install("python3")

    if (not run("which pip3")):
        install("python3-pip")

    if (not run("pip3 list | grep -io django")):
        result = run( "echo \'" + sudo + "\' | sudo -kS pip3 install django==1.8.4")
        print("Installed: Django")

    if (not run("which wget")):
        install("wget")

if __name__ == "__main__":
    env.host_string = host
    env.user = username
    env.password = password

    install_utils()
