#!/usr/bin/python3
"""
creates and distributes an archive to the webservers using
"""
from fabric.api import local, env, put, run
import os.path
from os.path import exists
from datetime import datetime

env.hosts = ["52.87.22.215", "100.25.153.47"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


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

        # remove existing contents of the release directory
        run("rm -rf {}".format(release_path))

        # create release directory
        run("mkdir -p {}".format(release_path))

        # extract the archive into the release directory
        run("tar -xzf /tmp/{} -C {}".format(filename, release_path))

        # delete the archive from the web server
        run("rm /tmp/{}".format(filename))

        # move the extracted files
        run("mv {}/web_static/* {}".format(release_path, release_path))

        # delete old symbolic link
        run("rm -rf /data/web_static/current")

        # create new symbolic link
        run("ln -s {} /data/web_static/current".format(release_path))

        print("New version deployed!")
        return True
    except Exception as e:
        return False


def deploy():
    archive_path = do_pack()
    if archive_path is None:
        return False
    deploy_result = do_deploy(archive_path)
    return deploy_result
