#!/usr/bin/env python
import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    lst = []
    for line in reader:
	data = line[4].strip()
	if data == '' or data == 'body':
	    continue
	try:
	    idx = data.index('>')
	    data = data[idx+1:0-(idx+2)]
	except:
	    pass
	lst.append(data)
	lst.sort(key = len)
	if len(lst) > 10:
	    lst.pop()
    for body in lst:
	print "{0}\t{1}".format(1, body)



if __name__ == "__main__":
    mapper()
