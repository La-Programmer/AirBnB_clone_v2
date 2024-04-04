#!/usr/bin/python3
from fabric.operations import local
from datetime import datetime
from fabric.api import run, put, sudo, env
import os

# Environment variable declaration
env.user = 'ubuntu'
env.hosts = ['54.209.112.14', '52.91.134.77']
env.key_filename = '~/.ssh/school'


def do_pack():
    """A function that generates a .tgz archive"""
    date = datetime.now()
    now = date.strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    try:
        result = local(
            'tar -czf versions/web_static_{}.tgz ./web_static'.format(now)
        )
        return "versions/web_static_{}.tgz".format(now)
    except Exception as e:
        return False


def do_deploy(archive_path):
    """Deploys an archive to web servers"""
    if not (os.path.exists(archive_path)):
        return False
    try:
        # Transfer archives
        put(archive_path, '/tmp/')

        # String variables
        archive_filename = run('ls /tmp/ | grep ".tgz"')
        extracted_filename = archive_filename.split('.')[0]
        path = '/data/web_static/releases'

        sudo(
            'mkdir -p /data/web_static/releases/{}'
            .format(extracted_filename)
        )
        sudo('rm -rf {}/{}'.format(path, extracted_filename))
        sudo('mkdir {}/{}'.format(path, extracted_filename))
        sudo(
            'tar -xzf /tmp/{} -C {}/{}'
            .format(archive_filename, path, extracted_filename)
        )
        run('rm /tmp/{}'.format(archive_filename))
        sudo(
            'mv {}/{}/web_static/* {}/{}'
            .format(path, extracted_filename, path, extracted_filename)
        )
        sudo('rm -rf {}/{}/web_static'.format(path, extracted_filename))
        sudo('rm -rf /data/web_static/current')
        sudo(
            'ln -s {}/{} /data/web_static/current'
            .format(path, extracted_filename)
        )
        return True
    except Exception as e:
        return False


def deploy():
    """Creates archives and distributes them to web servers"""
    archive = do_pack()
    if not (archive):
        return False
    else:
        return do_deploy(archive)
