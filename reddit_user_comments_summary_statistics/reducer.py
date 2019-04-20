#!/usr/bin/env python
import sys

def reducer():
    oldKey = None
    total_comments = 0
    total_ups = 0
    total_length = 0

    for line in sys.stdin:
	data = line.strip().split('\t')
		
	if len(data) != 3:
	    continue
	thisKey, ups, length = data
	if oldKey and thisKey != oldKey:
	    print "{}\t{}\t{}".format(oldKey, total_comments, total_ups/total_comments, total_length/total_comments)
	    total_comments = 0
	    total_ups = 0
	    total_length = 0
	oldKey = thisKey
	total_comments += 1
	total_ups += int(ups)
	total_length += int(length)
    if oldKey:
	print "{}\t{}\t{}\t{}".format(oldKey, total_comments, total_ups/float(total_comments), total_length/float(total_comments))
	

if __name__ == "__main__":
    reducer()
