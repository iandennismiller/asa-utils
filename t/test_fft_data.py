#!/usr/bin/python

import sys
sys.path.append('/Users/idm/Code/academic/asa-utils/lib')
from asa_utils import parse, amalgamate

f = '/Users/idm/Code/academic/asa-utils/t/data/single_band_test.asc'
t = parse(f)
print t.as_hash()

f = '/Users/idm/Code/academic/asa-utils/t/data/multiple_band_test.asc'
t = parse(f)
print t.as_hash()

