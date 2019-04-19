#!/usr/bin/env python
import sys
from datetime import datetime

def mapper():
    for line in sys.stdin:
	data = line.strip().split('\t')
	
	if len(data) != 6:
	    continue
	date, time, place, purchase_type, sale, card_type = data
	
	weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
	
	print "{0}\t{1}".format(weekday, sale)     

if __name__ == "__main__":
    mapper()
