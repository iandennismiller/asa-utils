from fabric.api import local
import os

def sdist():
    print local('cp wiki/ReadMe.wiki doc/README.TXT')
    print local('rm -rf build; python setup.py sdist --formats=gztar,zip')

def tag(ver):
    cmd = 'svn cp https://asa-utils.googlecode.com/svn/trunk/ https://asa-utils.googlecode.com/svn/tags/%s/'
    print local(cmd % ver)
