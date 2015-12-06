from yarn.api import env, cd, run
from private import host, username, password, sudo

import unittest



def install_utils():
    # install tmux
    if (not run("which tmux")):
        result = run( "echo \'" + sudo + "\' | sudo -kS apt-get -q -y --force-yes install tmux 2>&1")
        for line in result.lower().splitlines():
            if (line.startswith("e:")):
                print(result)
                exit()
        print ("Installed: tmux")


if __name__ == "__main__":
    env.host_string = host
    env.user = username
    env.password = password

    install_utils()
