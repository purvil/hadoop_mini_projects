#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

def mapper():
    for row in sys.stdin:
	row = row.strip()
	if not row.startswith('<row'):
	    continue
	
	parser = ET.fromstring(row)
	if parser.get('AnswerCount') > 0:
	    print "{0}\t{1}".format(parser.get('ViewCount'), parser.get('Score'))

if __name__ == "__main__":
    mapper()
