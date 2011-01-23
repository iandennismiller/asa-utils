# asa-utils
# (c) 2011 Ian Dennis Miller
# http://asa-utils.googlecode.com

import glob, logging, os
from Parse import Parse, ParseError

class EmptyDataFolder(Exception):
    pass

class Amalgamate(object):
    def __init__(self, path):
        self.path = path.rstrip()
        logging.getLogger('asa_utils').debug("Searching %s for data files" % self.path)
        self.files = glob.glob(os.path.join(self.path, "*"))
        logging.getLogger('asa_utils').debug("File list: %s" % self.files)
        if len(self.files) == 0:
            logging.getLogger('asa_utils').error("Directory does not exist, or is empty: %s" % path)
            raise EmptyDataFolder

    def run(self):
        self.parsers = []
        for file in self.files:
            try:
                p = Parse(file)
                self.parsers.append(p)
            except ParseError:
                logging.getLogger('asa_utils').warn("Failed to parse file: %s" % file)

        if len(self.parsers) == 0:
            logging.getLogger('asa_utils').error("Unable to parse any data files in this folder: %s" % self.path)
            raise EmptyDataFolder
        
        labels = self.parsers[0].as_hash()['amalgamate_labels']
        
        output = "filename\t%s\n" % '\t'.join(labels)
        
        for p in self.parsers:
            h = p.as_hash()
            output += "%s\t%s\n" % (h['filename'], '\t'.join(h['values']))
            
        return output
        