#!/usr/bin/env python
import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
	if line[0] == 'id':
	    continue
	data = line[4].strip() # accessing body
	data = re.sub('[^a-zA-Z]', ' ', data)
	for word in data.split():
	    if word == '' or word == ' ':
		continue
	    print "{0}\t{1}".format(word.lower(), line[0])

if __name__ == "__main__":
    mapper()
