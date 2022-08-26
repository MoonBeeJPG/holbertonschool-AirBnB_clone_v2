#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack """
from fabric.api import local
import datetime

def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        local("tar -cv2f versions/web_static_{}.tgz web_static".format(date))
            return("versions/web_static_{}.tgz".format(date))
    except Exception:
        return None
