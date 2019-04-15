#!/usr/bin/env python
import sys
def reducer():
    salesTotal = 0
    oldKey = None
    for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
	    continue
  	
	thisKey, thisSale = data
	
	if oldKey and thisKey != oldKey:
	    print "{0}\t{1}".format(oldKey, salesTotal)
	    salesTotal = 0
	oldKey = thisKey
  	salesTotal += float(thisSale)
    if oldKey:
	print "{0}\t{1}".format(oldKey, salesTotal)

if __name__ == "__main__":
    reducer()
