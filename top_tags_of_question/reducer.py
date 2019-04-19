#!/usr/bin/env python

import sys

def reducer():
    oldKey = None
    count = 0
    top_10 = []
    for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
	    continue
	thisKey, type_length = data
		
	if oldKey and oldKey != thisKey:
	    top_10.append((oldKey, count))
	    top_10.sort(key = lambda x:x[1], reverse=True)
	    count = 0
	    if len(top_10) > 10:
		top_10.pop()
	oldKey = thisKey
	count += 1
    if oldKey:
	top_10.append((oldKey, count))
        top_10.sort(key = lambda x:x[1], reverse=True)
        if len(top_10) > 10:
            top_10.pop()
    for tag, count in top_10:
	print "{0}\t{1}".format(tag, count)
if __name__ == "__main__":
    reducer()
