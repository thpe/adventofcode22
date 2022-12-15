#!/usr/bin/env python3
import sys
import numpy as np
import re
import copy



np.set_printoptions(threshold=sys.maxsize,linewidth=2000)

prog = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
segments = []

bcn = {}
sns = {}
#ref = 10
ref = 2000000
mark = {}
with open(sys.argv[1], 'r') as f:
  for l in f:
    l=l.strip()
    r = prog.match(l)
    coord = np.array([int(c) for c in r.groups()])
    print(coord)
    m = sum(np.abs(coord[0:2]-coord[2:4]))
    if coord[3] == ref:
        bcn[coord[2]] = 1
    if coord[1] == ref:
        sns[coord[0]] = 1
    d = coord[1] - ref
    dc = m - abs(d)
    print(f'manhatten {m} dist {d} diff {dc}')
    if abs(d) <= m:
        print(f'cut {dc}')
        for i in range(coord[0] - dc, coord[0] + dc+1):
            mark[i] = 1
#            print(f'mark {i}')
#        print (mark)

print(sns)
print(sum(mark.values()) - sum(bcn.values()) - sum(sns.values()))
mi = min(mark.keys())
ma = max(mark.keys())
print(f'{mi} -> {ma}')
#for i in range(mi, ma+1):
#    if i in mark.keys():
#        print('#', end='')
#    else:
#        print('.', end='')
#
print("\nend")
