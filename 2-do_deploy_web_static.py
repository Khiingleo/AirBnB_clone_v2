#!/usr/bin/python3
"""
distributes the archive from 1-pack_web_static to the web-servers
"""
from fabric.api import run, put, env
import os.path
from os.path import exists

env.user = "ubuntu"
env.hosts = ["100.25.153.47", "52.87.22.215"]
env.key_filename = "~/.ssh/id_rsa"

def do_deploy(archive_path):
    """
    distributes an archive to the web servers
    """
    if not exists(archive_path):
        return False

    try:
        # upload the archive to the /tmp/ directory of the server
        put(archive_path, '/tmp/')

        # uncompress the archive
        filename = os.path.basename(archive_path)
        file_w_e = filename.split(".")[0]
        release_path = "/data/web_static/releases/{}".format(file_w_e)
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(filename, release_path))

        # delete the archive from the web server
        run("rm /tmp/{}".format(filename))

        # move the extracted files
        run("mv {}/web_static/* {}".format(release_path, release_path))

        # delete old symbolic link
        run("rm -rf /data/web_static/current")

        # create new symbolic link
        run("ln -s {} /data/web_static/current".format(release_path))

        return True
    except Exception as e:
        return False
