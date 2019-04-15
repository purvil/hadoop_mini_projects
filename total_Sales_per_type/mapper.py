#!/usr/bin/env python
import sys

def mapper():
    for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 6:
	    continue
	date, time, city, purchase_type, cost, card = data
	print "{0}\t{1}".format(purchase_type, cost)

if __name__ == "__main__":
    mapper()
