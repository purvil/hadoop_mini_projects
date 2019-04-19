#!/usr/bin/env python

import sys

def reducer():
    oldTag = None
    total = 0
    count = 0
    for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
	    continue
	thisTag, answers = data
		
	if oldTag and thisTag != oldTag:
	    print "{0}\t{1}".format(oldTag, total/count)
	    total = 0
	    count = 0
	oldTag = thisTag
	count += 1
	total += float(answers)
    if oldTag:
	print "{0}\t{1}".format(oldTag, total/count)

	
if __name__ == "__main__":
    reducer()
