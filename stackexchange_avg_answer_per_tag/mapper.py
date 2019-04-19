#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

def mapper():
    for row in sys.stdin:
	row = row.strip()
	if not row.startswith('<row'):
	    continue
	parser = ET.fromstring(row)
	tags = parser.get('Tags')
	if tags:
	    tags = tags.replace('<', ' ')
	    tags = tags.replace('>', ' ')
	    tags = tags.strip().split()
	    for tag in tags:
		print "{0}\t{1}".format(tag, parser.get('AnswerCount'))

if __name__ == "__main__":
    mapper()
