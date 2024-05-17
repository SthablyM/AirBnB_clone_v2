#!/usr/bin/env bash
#script that generates a .tgz archive from the contents of the w
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """ Fabric script that generates a .tgz archive from the contents of the...
    ...web_static folder """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_ = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(file_))
    if result.succeeded:
        return file_
    else:
        return None
