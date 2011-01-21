# asa-utils
# (c) 2011 Ian Dennis Miller
# http://code.google.com/p/asa-utils/

import glob
from Parse import Parse

class Amalgamate(object):
    def __init__(self, path):
        self.path = path
        self.files = glob.glob('%s/*' % path)

    def run(self):
        parsers = []
        for file in self.files:
            p = Parse(file)
            parsers.append(p)
        
        labels = parsers[0].as_hash()['amalgamate_labels']
        
        print "filename\t", '\t'.join(labels)
        for p in parsers:
            h = p.as_hash()
            print h['filename'], "\t", '\t'.join(h['values'])
        