asa-utils
(c) 2011 Ian Dennis Miller

1. asa lab
----------

asa is a software package written by Advanced Neuro Technology (ANT):
http://www.ant-neuro.com/products/asa-lab

This software is unaffiliated with ANT.  

2. license
----------

This software is distributed according to the GNU Public License v2.  For 
license information, see LICENSE.TXT to read the full text of the GPLv2.

3. pre-requisites
-----------------

asa-utils requires Python.  This utility has been tested with Python 2.6, but
it is likely to work with Python 2.5 and 2.7 as well.

4. installation
---------------

To install asa-utils, do something like the following:

    sudo python setup.py install

5. usage
--------

To use asa-utils to combine many data files into one, first collect all of
the data files into a single directory, then use this syntax:

    asa-utils.py amalgamate some_directory > output.csv

6. support
----------

http://code.google.com/p/asa-utils/
