#!/usr/bin/env python

import sys

def reducer():
    oldKey = None
    total_sale_amount = 0
    total_sale_count = 0
    for line in sys.stdin:
	data = line.strip().split('\t')
	
	if len(data) != 2:
	    continue
	
	thisKey, thisSale = data

	if oldKey and oldKey != thisKey:
	    print "{0}\t{1}".format(oldKey, total_sale_amount/total_sale_count)
	    total_sale_amount = 0
	    total_sale_count = 0
	oldKey = thisKey
	total_sale_amount += float(thisSale)
	total_sale_count += 1
    
    if oldKey:
	print "{0}\t{1}".format(oldKey, total_sale_amount/total_sale_count)	

if __name__ == "__main__":
    reducer()
