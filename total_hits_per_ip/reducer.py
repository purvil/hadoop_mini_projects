#!/usr/bin/env python
import sys

def reducer():
    oldKey = None
    totalRequest = 0
    for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
	    continue
	thisKey, count = data
	if oldKey and oldKey != thisKey:
	    print "{0}\t{1}".format(oldKey, totalRequest)
	    totalRequest = 0
	oldKey = thisKey
	totalRequest += int(count)

    if oldKey:
	print "{0}\t{1}".format(oldKey, totalRequest)



if __name__ == "__main__":
    reducer()
