#!/usr/bin/env python3


import sys
import numpy as np
import re

def contain(r):
    if r[0] <= r[2] and r[1] >= r[3]:
        return True
    if r[2] <= r[0] and r[3] >= r[1]:
        return True
    return False


count = 0
prog = re.compile("([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)")
with open(sys.argv[1], 'r') as f:
  for l in f:
    l = l.strip()
    res = prog.match(l)
    r = [int(res.group(i)) for i in range(1,5)]
    if contain(r):
        count += 1
print (count)
