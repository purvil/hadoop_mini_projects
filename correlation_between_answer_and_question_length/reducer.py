#!/usr/bin/env python

import sys

def reducer():
    oldKey = None
    answer_length_total = 0
    answer_count = 0
    question_length = 0
    for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
	    continue
	thisKey, type_length = data
		
	if oldKey and oldKey != thisKey:
	    if answer_count != 0:
	        print "{0}\t{1}\t{2}".format(oldKey, question_length, answer_length_total/answer_count)
   	    else:
		print "{0}\t{1}\t{2}".format(oldKey, question_length, 0)
	    answer_count = 0
	    answer_length_total = 0
	oldKey = thisKey
	if type_length[0] == 'q':
	    question_length = int(type_length[1:])
	else:
	    answer_length_total += int(type_length[1:])
	    answer_count += 1
    if oldKey:
	if answer_count != 0:
	    print "{0}\t{1}\t{2}".format(oldKey, question_length, answer_length_total/answer_count)
	else:
	    print "{0}\t{1}\t{2}".format(oldKey, question_length, 0)

if __name__ == "__main__":
    reducer()
