#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers,
    using the function do_deploy """

from fabric.api import run, put, env
from os.path import exists

env.user = "ubuntu"
env.hosts = ['3.88.99.250', '184.73.123.157']


def do_deploy(archive_path):
    """Comment"""
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[1]
        filename_no_extension = filename.split(".")[0]
        file_path = "/data/web_static/releases/" + filename_no_extension + "/"
        run("mkdir -p " + file_path)
        run("tar -xzf /tmp/" + filename + " -C " + file_path)
        run("mv " + file_path + "web_static/*" + " " + file_path)
        run("rm /tmp/{}".format(filename))
        run("rm -rf " + file_path + "web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s " + file_path + " /data/web_static/current")
        print("New version deployed!")
        return True

    except Exception:
        return False
