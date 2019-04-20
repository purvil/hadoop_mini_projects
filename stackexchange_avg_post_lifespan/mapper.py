#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET
from datetime import datetime

def mapper():
    for row in sys.stdin:
	row = row.strip()
	if not row.startswith('<row'):
	    continue
	parser = ET.fromstring(row)
	first = parser.get('CreationDate')
	first_dt = datetime.strptime(first, "%Y-%m-%dT%X.%f")
	last = parser.get('LastActivityDate')
        last_dt = datetime.strptime(last, "%Y-%m-%dT%X.%f")
	
	print "{0}\t{1}".format((last_dt-first_dt).days, 1)
if __name__ == "__main__":
    mapper()
