#!/usr/bin/env python
import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
	if len(line) != 19:
	   continue
	idx, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
	if not parent_id.strip()  or abs_parent_id == '\N':
	    print "{0}\t{1}".format(idx, author_id)
	else:
	    print "{0}\t{1}".format(abs_parent_id, author_id)

if __name__ == "__main__":
    mapper()
