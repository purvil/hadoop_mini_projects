#!/usr/bin/env python

import sys

def reducer():
    oldKey = None
    lst = []
    for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
	    continue
	thisKey, author = data
		
	if oldKey and oldKey != thisKey:
	    print "{0}\t{1}".format(oldKey, ", ".join(lst))
	    lst = []
    	oldKey = thisKey
	lst.append(author)
    if oldKey:
	print "{0}\t{1}".format(oldKey, ", ".join(lst))
    
if __name__ == "__main__":
    reducer()
