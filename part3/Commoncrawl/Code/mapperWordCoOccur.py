#!/usr/bin/env python
"""mapper.py"""
import sys
top10 = ['health mental disorder brain science study human program treatment clinical']
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = line.lower()
    # split the line into words
    words = line.split()
    # increase counters
    for each in top10[0].split(' '):
        if each in words:
            for i in words:
                if i != each:
                    temp = []
                    temp.append(each)
                    temp.append(i)
                    temp.sort()
                    print '%s,%s\t%s' % (temp[0], temp[1], 1)

