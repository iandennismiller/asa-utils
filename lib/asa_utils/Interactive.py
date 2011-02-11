# asa-utils
# (c) 2011 Ian Dennis Miller
# http://asa-utils.googlecode.com

from Amalgamate import Amalgamate, EmptyDataFolder
import sys, platform, re, os, logging, datetime

class Interactive(object):
    def __init__(self):
        pass

    def run(self):
        c = ''
        while c.upper() not in ['Q']:
            print "\n[asa-utils main menu]\n"
            print "(a) Amalgamate several data files into a single spreadsheet"
            print "(d) Turn on debugging output"
            print "(q) Quit"

            c = raw_input("> ")
        
            if c.upper() == 'A':
                source_path = raw_input("Enter the path of the data folder: ")
                out_path = os.path.expanduser('~')
                if re.search(r'^Windows', platform.platform()):
                    out_path = os.path.join(out_path, 'Desktop')
                now = datetime.datetime.now()
                timestamp = "%s-%0.2d-%0.2d-%0.2d-%0.2d-%0.2d" % \
                    (now.year, now.month, now.day, now.hour, now.minute, now.second)
                output_file = os.path.join(out_path, "asa-utils_%s.csv" % timestamp)

                m = re.match(r'"(.*)"', source_path) 
                if m:
                    source_path = m.group(1)
                source_path = source_path.replace('\ ', ' ')

                try:
                    a = Amalgamate(source_path)
                    (results, meta) = a.run()
                    a.export_csv(results, meta, output_file)
                except EmptyDataFolder:
                    continue
            elif c.upper() == 'D':
                logging.getLogger('asa_utils').setLevel(logging.DEBUG)
                print "Debugging is enabled"
