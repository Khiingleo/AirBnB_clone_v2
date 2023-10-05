#!/usr/bin/python3
"""
fabric script that deletes out of date archives
(based on 3-deploy_web_static)
"""
import os.path
from fabric.api import *

env.hosts = ["100.25.153.47", "52.87.22.215"]
env.user = "ubuntu"


def do_clean(number=0):
    """
    deletes out-of-date archives
    """
    try:
        number = int(number)
        if number < 0:
            return False
    except ValueError:
        return False

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        for a in archives:
            [local("rm ./{}".format(a))]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
