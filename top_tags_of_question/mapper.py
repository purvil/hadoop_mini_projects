#!/usr/bin/env python
import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
	if len(line) != 19:
	   continue
	idx, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
	if node_type == 'question':
	    for tag in tagnames.split():
	        print "{0}\t{1}".format(tag, 1)

if __name__ == "__main__":
    mapper()
