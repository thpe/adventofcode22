#!/usr/bin/env python3
import sys
import numpy as np
import re
import copy



prog = re.compile(r'([0-9]*)')
prog = re.compile(r'^(?:(?:[\[\],])*([\d]+)*(?:(?:[\[\],])*))$')


last = []
row = 1
cnt = 0
def compare(l,r):
    res = 0
    if not isinstance(l, list) and not isinstance(r, list):
        if l < r:
            return -1
        if l == r:
            return 0
        return 1

    if not isinstance(l, list):
        l = [l]
    if not isinstance(r, list):
        r = [r]

    if len(l) > 0 and len(r) == 0:
        return 1

    if len(l) == 0 and len(r) == 0:
        return 0

    if len(l) == 0 and len(r) > 0:
        return -1



    res = compare(l[0], r[0])
    if res == 0:
        res = compare(l[1:],r[1:])
    return res


def readlist(l):
    r = []
    val = None
    while (len(l) > 0):
        c = l.pop(0)
        if c == '[':
            r.append(readlist(l))
        elif c == ']':
            if val is not None:
                r.append(val)
            return r
        elif c == ',':
            if val is not None:
                r.append(val)
            val = None
        else:
            if val is None:
                val = int(c)
            else:
                val = (val * 10) + int(c)
    return r

with open(sys.argv[1], 'r') as f:
  for l in f:
    l = [c for c in l.strip()]
    if len(l) == 0:
        pass
    else:
        last.append(readlist(l))

last.append([[2]])
last.append([[6]])
cpy = copy.deepcopy(last)

for i in range(int(len(last)/2)):
    l = last[2*i]
    r = last[2*i+1]
    if compare(l,r) >= 0:
        cnt += i+1


import functools
cpy.sort(key=functools.cmp_to_key(compare))
val = [0,0]
for i in range(len(cpy)):
    if cpy[i] == [[2]]:
        print(f'found 2 at {i+1}')
        val[0] = i+1
    if cpy[i] == [[6]]:
        print(f'found 6 at {i+1}')
        val[1] = i+1
print(f'solution 1 {val[0]*val[1]}')
