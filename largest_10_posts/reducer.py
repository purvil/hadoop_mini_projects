#!/usr/bin/env python
import sys

def reducer():
    lst = []
    for line in sys.stdin:
	data = line.strip().split('\t')
	
	if len(data) != 2:
	    continue
	
	lst.append(data[1])
	lst.sort(key=len, reverse=True)
	if len(lst) > 10:
	    lst.pop()
    for body in lst:
	print(body)
	


if __name__ == "__main__":
    reducer()
