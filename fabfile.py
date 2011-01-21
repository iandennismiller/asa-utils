from fabric.api import local
import os

def sdist():
    print local('cp wiki/ReadMe.wiki doc/README.TXT; cp wiki/InstallHelp.wiki doc/INSTALL.TXT')
    print local('rm -rf build; python setup.py sdist --formats=gztar,zip')

def tag():
    ver = local('python setup.py --version').rstrip()
    cmd = 'svn cp https://asa-utils.googlecode.com/svn/trunk/ https://asa-utils.googlecode.com/svn/tags/%s/'
    os.system(cmd % ver)
