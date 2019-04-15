#!/usr/bin/env python
import sys

def reducer():
    totalCount = 0
    totalSale = 0
    for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
	    continue
	count, thisSale = data
	totalCount += float(count)
	totalSale += float(thisSale)
    print "{0}\t{1}".format(totalCount, totalSale)

if __name__ == "__main__":
    reducer()
