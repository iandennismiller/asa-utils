#!/usr/bin/python

# asa-utils
# (c) 2011 Ian Dennis Miller
# http://code.google.com/p/asa-utils/

import sys
sys.path.append('/Users/idm/Code/academic/asa-utils/lib')

def test_parse():
    from asa_utils.Parse import Parse
    f = '/Users/idm/Code/academic/asa-utils/t/data/single_band_test.asc'
    t = Parse(f)
    print t.as_hash()

    f = '/Users/idm/Code/academic/asa-utils/t/data/multiple_band_test.asc'
    t = Parse(f)
    print t.as_hash()

def test_amalgamate():
    from asa_utils.Amalgamate import Amalgamate
    path = '/Users/idm/Code/academic/asa-utils/t/data/amalgam'
    a = Amalgamate(path)
    print a.run()    

#test_parse()
test_amalgamate()