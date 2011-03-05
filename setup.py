#!/usr/bin/env python

import platform, re, sys, os, shutil
from distutils.core import setup

if re.search(r'^Windows', platform.platform()):
    sys.argv[1:] = ['install']
    print "\nPerforming Windows-specific installation"
    c = raw_input("press enter to start...")
    home_path = os.path.expanduser('~')
    install_path = os.path.join(home_path, 'Start Menu', 'Programs', 'ASA Utils')
    try:
        os.mkdir(install_path)
    except WindowsError:
        pass

    asa_util_bin = os.path.join(os.getcwd(), 'bin', 'asa-utils.py')
    shutil.copy(asa_util_bin, install_path)
    print "Installed asa-utils to the start menu."

setup(name='asa_utils',
    version='0.2.4',
    description = "process data files generated by ANT's asa-lab EEG suite",
    author = 'Ian Dennis Miller',
    author_email = 'ian@saperea.com',
    url = 'http://asa-utils.googlecode.com',
    packages=['asa_utils'],
    long_description= """
    Process data files generated by Advanced Neuro Technology's asa-lab EEG suite. 
    This utility will combine results from multiple participants into a single 
    data file for statistical analysis.""",
    package_dir = {'': 'lib'},
    scripts=['bin/asa-utils.py'],
    license="GPL v2",
    platforms = ["any"],
)

if re.search(r'^Windows', platform.platform()):
    print "\nInstallation successful.  You can now find asa-utils in the start menu."
    c = raw_input("press enter to finish...")
