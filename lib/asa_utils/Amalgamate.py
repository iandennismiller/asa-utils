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

    "given a list of parser objects, figure out an authoritative listing of columns"
    def infer_colnames(self):
        names = set()
        for p in self.parsers:
            for c in p.as_hash()['amalgamate_labels']:
                names.add(c)
        for p in self.parsers:
            if len(p.as_hash()['amalgamate_labels']) == len(names):
                return p.as_hash()['amalgamate_labels']
        return names

    def run(self):
        #labels = self.parsers[0].as_hash()['amalgamate_labels']
        labels = self.infer_colnames()

        result = []
        row = ['filename']
        row.extend(labels)
        row.append('epochs')
        result.append(row)
        for p in self.parsers:
            h = p.as_hash()
            row = [h['filename']]
            #row.extend(h['values'])
            for key in labels:
                if key in h['data']:
                    row.append(h['data'][key])
                else:
                    row.append("null")
            row.append(h['epochs'])
            result.append(row)

        #meta = ["__meta__", "version", 1, 
        #    "sampling frequency", self.parsers[0].sampling_frequency,
        #    "epoch length", self.parsers[0].epoch_length,
        #    "epochs per channel", self.parsers[0].epochs,
        #    ]

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
        #writer.writerow(meta_info)
        for row in results:
            writer.writerow(row)
        f.close()
