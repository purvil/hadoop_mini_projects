#!/usr/bin/env python
import sys

def mapper():
    for line in sys.stdin:
	data = line.strip().split(' ')
	if len(data) != 10:
	    continue
	map(str.strip, data)
	ip, client_id, client_uname, date, tz, method, resource, protocol, status_code, size = data  
	date = date[1:]
	method = method[1:]
	protocol = protocol[:-1]
	tz = tz[:-1]
	print "{0}\t{1}".format(resource, 1)


if __name__ == "__main__":
    mapper()
