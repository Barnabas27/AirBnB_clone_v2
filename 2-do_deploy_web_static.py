#!/usr/bin/python3
""" deploy with fabric of static files of aribnb
"""

from fabric.api import *
from os import path


env.hosts = ['3.236.4.92', '3.239.83.251']


def do_deploy(archive_path):
    """Deploy the airbnb static
    """
    if not path.exists(archive_path):
        return False
    ret_value = True
    d_folder = put(archive_path, '/tmp/')
    if d_folder.failed:
        ret_value = False
    archive_file = archive_path.replace(".tgz", "").replace("versions/", "")
    d_dest = run('mkdir -p /data/web_static/releases/' + archive_file + '/')
    if d_dest.failed:
        ret_value = False
    d_unpack = run('tar -xzf /tmp/' + archive_file + '.tgz' +
                   ' -C /data/web_static/releases/' + archive_file + '/')
    if d_unpack.failed:
        ret_value = False
    d_cleanfile = run('rm /tmp/' + archive_file + '.tgz')
    if d_cleanfile.failed:
        ret_value = False
    d_move = run('mv /data/web_static/releases/' + archive_file +
                 '/web_static/* /data/web_static/releases/' + archive_file +
                 '/')
    if d_move.failed:
        ret_value = False
    d_cleanfolder = run('rm -rf /data/web_static/releases/' + archive_file +
                        '/web_static')
    if d_cleanfolder.failed:
        ret_value = False
    d_removeold = run('rm -rf /data/web_static/current')
    if d_removeold.failed:
        ret_value = False
    d_createnew = run('ln -sf /data/web_static/releases/' + archive_file +
                      '/' + ' /data/web_static/current')
    if d_createnew.failed:
        ret_value = False
    if ret_value:
        print("All tasks succeeded!")
    return ret_value