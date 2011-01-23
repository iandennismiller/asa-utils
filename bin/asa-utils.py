#!/usr/bin/env python

# asa-utils
# (c) 2011 Ian Dennis Miller
# http://asa-utils.googlecode.com

import sys, platform, re, logging

def do_interactive():
    from asa_utils.Interactive import Interactive
    i = Interactive()
    i.run()

def do_amalgamate():
    from asa_utils.Amalgamate import Amalgamate, EmptyDataFolder
    path = sys.argv[2]
    a = Amalgamate(path)
    try:
        print a.run()
    except EmptyDataFolder:
        print "Data folder appears to contain no data files?"

def parse_cmdline():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'amalgamate':
            do_amalgamate()
        elif sys.argv[1] == 'interactive':
            do_interactive()
    else:
        print """
    usage:
    asa-utils [command] [directory]

    example:
    asa-utils amalagamate data_directory > output.csv

    example:
    asa-utils interactive
    """

if __name__ == '__main__':
    console = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s\t%(message)s')
    console.setFormatter(formatter)
    logging.getLogger('asa_utils').addHandler(console)
    logging.getLogger('asa_utils').setLevel(logging.INFO)

    if re.search(r'^Windows', platform.platform()):
        do_interactive()
    else:
        parse_cmdline()
