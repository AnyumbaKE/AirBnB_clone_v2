#!/usr/bin/python3
"""
Deletes out-of-date archives, using the function do_clean
"""

import os
from fabric.api import *


env.hosts = ["54.237.218.228", "34.204.101.100"]


def do_clean(number=0):
    """Deletes out-of-date archives of the static files."""

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
