#!/usr/bin/env python
import sys

def reducer():
    oldKey = None
    total = 0
    for line in sys.stdin:
	data = line.strip().split('\t')
	
	if len(data) != 2:
	    continue
	thisKey, thisVal = data

	if oldKey and oldKey != thisKey:
	    print "{0}\t{1}".format(oldKey, total)
	    total = 0
	oldKey = thisKey
	total += int(thisVal)
    if oldKey:
	print "{0}\t{1}".format(oldKey, total)

if __name__ == "__main__":
    reducer()
