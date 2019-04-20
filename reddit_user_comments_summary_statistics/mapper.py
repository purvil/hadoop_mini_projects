#!/usr/bin/env python

import sys
import csv

def mapper():
    for row in sys.stdin:
        #row = row.strip()
        data = next(csv.reader([row], delimiter='\t'))

        if len(data) != 8:
            continue

        sub, author, body, creation_time, ups, downs, gilded, archived = data

        
        print('{0}\t{1}\t{2}'.format(author, ups, len(body)))

if __name__ == "__main__":
    mapper()
