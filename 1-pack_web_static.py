#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder using do_pack
"""
from fabric.operations import local
from datetime import datetime


def do_pack():
    """
    generates a .tgz from web_static folder
    """
    current_time = datetime.utcnow()
    archive_name = "web_static_{}.tgz".format(
                    current_time.strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    filename = "versions/{}".format(archive_name)
    result = local("tar -czvf {} web_static/".format(filename))
    if result.succeeded:
        return filename
    else:
        return None
