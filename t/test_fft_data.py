#!/usr/bin/python

# asa-utils
# (c) 2011 Ian Dennis Miller
# http://code.google.com/p/asa-utils/

import sys, unittest
from nose.plugins.attrib import attr
sys.path.append('/Users/idm/Code/saperea/asa-utils/lib')

@attr(priority=1)
def test_parse():
    from asa_utils.Parse import Parse
    f = '/Users/idm/Code/saperea/asa-utils/t/data/single_band_test.asc'
    t = Parse(f)
    assert t.as_hash()

    f = '/Users/idm/Code/saperea/asa-utils/t/data/multiple_band_test.asc'
    t = Parse(f)
    assert t.as_hash()

@attr(priority=1)
def test_amalgamate():
    from asa_utils.Amalgamate import Amalgamate
    path = '/Users/idm/Code/saperea/asa-utils/t/data/amalgam'
    a = Amalgamate(path)
    results = a.run()
    assert results
    as_str = a.as_string(results)
    assert as_str

@attr(priority=1)
def test_empty_amalgamate():
    from asa_utils.Amalgamate import Amalgamate, EmptyDataFolder
    path = '/Users/idm/Code/saperea/asa-utils/t/data/empty'
    a = Amalgamate(path)
    try:
        results = a.run()
        assert False
    except EmptyDataFolder:
        pass

@attr(priority=1)
def test_bad_parse():
    from asa_utils.Parse import Parse, ParseError
    f = '/Users/idm/Code/saperea/asa-utils/t/data/error_parse.asc'
    try:
        t = Parse(f)
        assert False
    except ParseError:
        pass

@attr(priority=1)
def test_folder_with_errors():
    from asa_utils.Amalgamate import Amalgamate
    path = '/Users/idm/Code/saperea/asa-utils/t/data/contains_errors'
    a = Amalgamate(path)
    results = a.run()
    assert results

def test_csv_export():
    from asa_utils.Amalgamate import Amalgamate
    path = '/Users/idm/Code/saperea/asa-utils/t/data/amalgam'
    a = Amalgamate(path)
    (results, meta) = a.run()
    a.export_csv(results, meta, '/tmp/out.csv')
