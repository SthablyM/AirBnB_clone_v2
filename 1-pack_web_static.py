#!/usr/bin/env bash
#script that generates a .tgz archive from the contents of the w
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    if not os.path.exists("versions"):
        os.makedirs("versions")

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    archive_name = f"web_static_{timestamp}.tgz"
    archive_path = f"versions/{archive_name}"

    try:
        local(f"tar -cvzf {archive_path} web_static")
        print(f"Archive created: {archive_path}")
        return archive_path
    except:
        print("An error occurred while creating the archive")
        return None
