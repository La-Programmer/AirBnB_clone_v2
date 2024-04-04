#!/usr/bin/python3
# Automates the deploy of web servers
from fabric.api import run, put, sudo, env
import os


# Environment variable declaration
env.user = 'ubuntu'
env.hosts = ['54.209.112.14', '52.91.134.77']
env.key_filename = '~/.ssh/school'


# Deployment function
def do_deploy(archive_path):
    """Deploys an archive to web servers"""
    if not (os.path.exists(archive_path)):
        return False
    try:
        put(archive_path, '/tmp/')
        archive_filename = run('ls /tmp/ | grep ".tgz"')
        extracted_filename = archive_filename.split('.')[0]
        print(archive_filename, extracted_filename)
        sudo(
            'mkdir -p /data/web_static/releases/{}'
            .format(extracted_filename)
        )
        sudo(
            'tar -xzf /tmp/{} -C /data/web_static/releases/{}'
            .format(archive_filename, extracted_filename)
        )
        run('rm /tmp/{}'.format(archive_filename))
        sudo('rm -rf /data/web_static/current')
        sudo(
            'ln -s /data/web_static/current /data/web_static/releases/{}'
            .format(extracted_filename)
        )
        return True
    except Exception as e:
        print("An error occurred: ", e)
        return False
