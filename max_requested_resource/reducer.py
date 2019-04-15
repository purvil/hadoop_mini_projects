#!/usr/bin/env python
import sys

def reducer():
    oldKey = None
    ansKey = None
    ansRequest = 0
    totalRequest = 0
    for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
	    continue
	thisKey, count = data
	if oldKey and oldKey != thisKey:
	    if totalRequest > ansRequest:
		ansRequest = totalRequest
		ansKey = oldKey	    
	    totalRequest = 0
	oldKey = thisKey
	totalRequest += int(count)

    if oldKey:
	if totalRequest > ansRequest:
       	    ansRequest = totalRequest
            ansKey = oldKey
    print "{0}\t{1}".format(ansKey, ansRequest)


if __name__ == "__main__":
    reducer()
