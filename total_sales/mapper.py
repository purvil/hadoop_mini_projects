#!/usr/bin/env python
import sys

def mapper():
    for line in sys.stdin:
	data = line.strip().split('\t')
	
	if len(data) != 6:
	    continue
	
	date, time, store, saleType, thisSale, cardType = data

	print "{0}\t{1}".format(1, thisSale)

if __name__ == "__main__":
    mapper()
