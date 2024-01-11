#!/usr/bin/python3
""" A Fabric script that generates a .tgz """

from datetime import datetime
from fabric.api import local
from fabric.decorators import runs_once


@runs_once
def do_pack():
    """ This generates a tgz archive from web_static folder """
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static"
                   .format(path))

    if result.failed:
        return None
    return path
