#!/usr/bin/env python

# asa-utils
# (c) 2011 Ian Dennis Miller
# ian@saperea.com

import sys

if sys.argv[1] == 'amalgamate':
    from asa_utils.Amalgamate import Amalgamate
    path = sys.argv[2]
    a = Amalgamate(path)
    print a.run()    
