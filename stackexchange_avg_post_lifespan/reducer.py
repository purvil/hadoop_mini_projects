#!/usr/bin/env python

import sys

def reducer():

    total = 0
    count = 0
    for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
	    continue
	total += int(data[0])
	count += 1
    print "{0}".format(total/float(count))

	
if __name__ == "__main__":
    reducer()
