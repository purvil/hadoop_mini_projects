#!/usr/bin/env python
import sys

def reducer():
    curMax = 0
    oldKey = None
	
    for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
	    continue

	thisKey, thisCost = data

	if oldKey and oldKey != thisKey:
	    print "{0}\t{1}".format(oldKey, curMax)
	    curMax = 0
	oldKey = thisKey
	if curMax < float(thisCost):
	    curMax = float(thisCost)
    if oldKey:
	print "{0}\t{1}".format(oldKey, curMax)

if __name__ == "__main__":
    reducer()
