# asa-utils
# (c) 2011 Ian Dennis Miller
# http://asa-utils.googlecode.com

from Amalgamate import Amalgamate, EmptyDataFolder
import sys, platform, re, os, logging

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

                m = re.match(r'"(.*)"', source_path) 
                if m:
                    source_path = m.group(1)
                source_path = source_path.replace('\ ', ' ')

                try:
                    a = Amalgamate(source_path)
                    results = a.run()
                except EmptyDataFolder:
                    continue
                
                output_file = os.path.join(out_path, "asa-utils.csv")
                logging.getLogger('asa_utils').info("Output file is %s" % output_file)
                f = open(output_file, 'w')
                f.write(results)
                f.close()
            elif c.upper() == 'D':
                logging.getLogger('asa_utils').setLevel(logging.DEBUG)
                print "Debugging is enabled"
