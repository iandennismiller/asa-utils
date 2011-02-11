# asa-utils
# (c) 2011 Ian Dennis Miller
# http://asa-utils.googlecode.com

from __future__ import with_statement
import csv, sys, re, logging

class ParseError(Exception):
    pass

class Parse(object):
    def __init__(self, filename):
        self.filename = filename
        logging.getLogger('asa_utils').debug("attempting to parse %s" % self.filename)
        with open(self.filename) as f:
            data_file = csv.reader(f, delimiter='\t')
            self.read_file(data_file)
            
    def read_file(self, data_file):
        # verify data export file type
        ident = data_file.next()[0]
        if ident != '# Time Frequency Data Export':
            logging.getLogger('asa_utils').error("data file does not appear to be Time Frequency Data")
            raise ParseError
            
        # skip metadata
        for i in range(0, 8):
            data = data_file.next()
            if i == 3:
                self.sampling_frequency = float(data[1])
            elif i == 4:
                self.epoch_length = float(data[1])
            elif i == 5:
                self.epochs = int(data[1])
        
        # determine number of bands
        band_count_line = data_file.next()
        if band_count_line[0] == 'NumberOfBands=':
            self.band_count = int(band_count_line[1])
        else:
            logging.getLogger('asa_utils').error("unable to determine number of bands in data")
            raise ParseError
        
        # remove BandsData
        data_file.next()
        # remove BandsData ranges
        for i in range(0, self.band_count):
            data_file.next()
        # remove newline
        data_file.next()

        if data_file.next()[0] != 'BandsNames':
            logging.getLogger('asa_utils').error("unable to determine name of bands in data")
            raise ParseError
        
        self.bands_names = []
        for i in range(0, self.band_count):
            self.bands_names.append(data_file.next()[0].replace(' ', '_'))
        
        # determine number of channels
        channel_count_line = data_file.next()
        if channel_count_line[0] == 'NumberOfChannels=':
            self.channel_count = int(channel_count_line[1])
        else:
            logging.getLogger('asa_utils').error("unable to determine number of channels in data")
            raise ParseError
        
        # skip unit measure
        data_file.next()
        # skip ValuesTransposed
        data_file.next()

        # read values
        self.values = []
        for i in range(0, self.band_count):
            values_read = data_file.next()
            if re.search(r'\:$', values_read[0]):
                values_read.pop(0)
            for j in range(0, self.channel_count):
                self.values.append(float(values_read[j]))

        # skip number of data sets
        data_file.next()
        data_file.next()
        
        # get filename
        self.data_filename = data_file.next()[0]

        # skip Labels
        data_file.next()

        self.labels = []
        # read Label names
        labels_read = data_file.next()
        for i in range(0, self.channel_count):
            self.labels.append(labels_read[i])
            
        # amalgamate labels
        if self.band_count > 1:
            self.amalgamate_labels = []
            for band_name in self.bands_names:
                for label in self.labels:
                    self.amalgamate_labels.append('%s_%s' % (band_name, label))
        else:
            self.amalgamate_labels = self.labels
        
        logging.getLogger('asa_utils').debug("successfully parsed %s" % self.filename)
        
    def as_hash(self):
        h = {
            'band_count': self.band_count,
            'bands_names': self.bands_names,
            'channel_count': self.channel_count,
            #'filename': self.data_filename,
            'filename': self.filename,
            'labels': self.labels,
            'values': self.values,
            'amalgamate_labels': self.amalgamate_labels,
        }
        return h
