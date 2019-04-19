#!/usr/bin/env python

import sys

def reducer():
    oldKey = None
    d = dict()
    for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
	    continue
	thisKey, hr = data
		
	if oldKey and oldKey != thisKey:
	    max_occurence = max(d.values())
	    for hour in d.keys():
		if d[hour] == max_occurence:
		    print "{0}\t{1}".format(oldKey, hour)
	    d = dict()
	oldKey = thisKey
	if hr not in d:
	    d[hr] = 1
	else:
	    d[hr] += 1
    if oldKey:
	max_occurence = max(d.values())
	for hour in d.keys():
	    if d[hour] == max_occurence:
		print "{0}\t{1}".format(oldKey, hour)

if __name__ == "__main__":
    reducer()
