# asa-utils
# (c) 2011 Ian Dennis Miller
# http://asa-utils.googlecode.com

import glob, logging, os, csv
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
        
        result = []
        row = ['filename']
        row.extend(labels)
        result.append(row)
        for p in self.parsers:
            h = p.as_hash()
            row = [h['filename']]
            row.extend(h['values'])
            result.append(row)

        return result

    def as_string(self, results):
        output = ""
        for row in results:
            output += "%s\n" % '\t'.join(str(i) for i in row)
        return output
    
    def export_csv(self, results, output_file):
        logging.getLogger('asa_utils').info("Output file is %s" % output_file)
        f = open(output_file, 'wb')
        writer = csv.writer(f, dialect='excel')
        #writer = csv.writer(f, delimiter=',', quotechar='"', 
        #    doublequote=True, skipinitialspace = False, 
        #    lineterminator = '\r\n', quoting = csv.QUOTE_NONNUMERIC)
        for row in results:
            writer.writerow(row)
        f.close()
