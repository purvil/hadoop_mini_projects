#!/usr/bin/env python
import sys

def reducer():
    oldKey = None
    idx = set()
    for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
	    continue
	thisKey, thisId = data

	if oldKey and oldKey != thisKey:
	    lst = list(idx)
	    lst.sort(key=int)
	    print "{0}\t{1}".format(oldKey, " ".join(lst))
	    idx = set()
	oldKey = thisKey
	idx.add(thisId)
    if oldKey:
	lst = list(idx)
	lst.sort(key=int)
        print "{0}\t{1}".format(oldKey, " ".join(lst))

if __name__ == "__main__":
    reducer()
