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
            return 1
        if l == r:
            return 0
        return -1

    if not isinstance(l, list):
        l = [l]
    if not isinstance(r, list):
        r = [r]

    if len(l) > 0 and len(r) == 0:
        return -1

    if len(l) == 0 and len(r) == 0:
        return 0

    if len(l) == 0 and len(r) > 0:
        return 1



    while len(l) > 0 and res == 0:
        lc = l.pop(0)
        lr = r.pop(0)
        res = compare(lc, lr)
        if res == 0:
            res = compare(l,r)
    return res


def readlist(l):
    r = []
    val = None
    while (len(l) > 0):
        c = l.pop(0)
        if c == '[':
            r.append(readlist(l))
#            print(f'decent got {r[-1]}')
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
        print (l)
        last.append(readlist(l))
        print(last[-1])

cpy = copy.deepcopy(last)

for i in range(int(len(last)/2)):
    l = last[2*i]
    r = last[2*i+1]
    if compare(l,r) >= 0:
        print(f'{l} >= {r}')
        cnt += i+1
    else:
        print(f'{l} < {r}')
print(cnt)

