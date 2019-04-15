#!/usr/bin/env python
import sys

def reducer():
    oldType = None
    totalSales = 0
    for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
	    continue

	thisType, thisSale = data

	if oldType and oldType != thisType:
	    print "{0}\t{1}".format(oldType, totalSales)
	    totalSales = 0
	
	oldType = thisType
	totalSales += float(thisSale)
    if oldType:
	print "{0}\t{1}".format(oldType, totalSales)

if __name__ == "__main__":
    reducer()
