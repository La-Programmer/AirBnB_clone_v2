#!/usr/bin/python3
from fabric.operations import local
from datetime import datetime


def do_pack():
    """A function that generates a .tgz archive"""
    date = datetime.now()
    now = date.strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    result = local(
        'tar -czf versions/web_static_{}.tgz ./web_static'.format(now)
    )
    print(result)
