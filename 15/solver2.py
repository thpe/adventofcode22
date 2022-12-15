#!/usr/bin/env python3
import sys
import numpy as np
import re
import copy
from tqdm import tqdm



np.set_printoptions(threshold=sys.maxsize,linewidth=2000)

prog = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
segments = []


bd = {}
bcn = {}
sns = []
#ref = 10
ref = 2000000
mark = {}

def check(x,y):
    minv = 0
    #maxv = 20
    maxv = 4000000
    return x >= minv and x <= maxv and y >=minv and y <= maxv

def checksensor(x,y, sns):
    v = np.array([x,y])
    overlap = False
    for s in sns:
        sens = s[0]
        m = s[1]
        if np.sum(np.abs(sens-v)) <= m:
            overlap = True
            break
    return overlap

with open(sys.argv[1], 'r') as f:
  for l in f:
    l=l.strip()
    r = prog.match(l)
    coord = np.array([int(c) for c in r.groups()])
    print(coord)
    m = sum(np.abs(coord[0:2]-coord[2:4]))
    sns.append((coord[0:2],m))
    d = coord[1] - ref
    dc = m - abs(d)
    print(f'manhatten {m} dist {d} diff {dc} size {len(bd.values())}')
    m = m+1
    for i in tqdm(range(m+1)):
        ix = coord[0]+i
        iy = coord[1]-(m-i)
        idx = f'{ix},{iy}'
        if check(ix,iy) and not checksensor(ix,iy, sns):
            bd[idx] = np.array([ix,iy])
        iy = coord[1]+(m-i)
        idx = f'{ix},{iy}'
        if check(ix,iy) and not checksensor(ix,iy, sns):
            bd[idx] = np.array([ix,iy])
        ix = coord[0]-i
        iy = coord[1]-(m-i)
        idx = f'{ix},{iy}'
        if check(ix,iy) and not checksensor(ix,iy, sns):
            bd[idx] = np.array([ix,iy])
        iy = coord[1]+(m-i)
        idx = f'{ix},{iy}'
        if check(ix,iy) and not checksensor(ix,iy, sns):
            bd[idx] = np.array([ix,iy])

with open(sys.argv[1], 'r') as f:
  for l in f:
    l=l.strip()
    r = prog.match(l)
    coord = np.array([int(c) for c in r.groups()])
    m = sum(np.abs(coord[0:2]-coord[2:4]))
    sens = coord[0:2]
    popkey = []
    for k,v in bd.items():
       if np.sum(np.abs(sens-v)) <= m:
#            print(f'{sens} {v} -> {np.sum(np.abs(sens-v))} < {m}')
            popkey.append(k)

#    print(popkey)
    for k in popkey:
        bd.pop(k, None)
    print(f'sensor {coord[0:2]} {m} size {len(bd.values())}')
#    if '14,11' in bd.keys():
#        print('  ok')




print(bd)
maxkey = max(bd, key=bd.get)
print(maxkey)
x = bd[maxkey][0]
y = bd[maxkey][1]
print(f'{x*4000000+y}')
