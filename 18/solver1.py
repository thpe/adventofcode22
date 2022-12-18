#!/usr/bin/env python3
import sys
import numpy as np
import re
import copy
from tqdm import tqdm
import functools

def compare(a,b):
    idx = 0
    if a[idx] < b[idx]:
        return -1
    elif a[idx] > b[idx]:
        return 1
    else:
        return 0


np.set_printoptions(threshold=sys.maxsize,linewidth=2000)

pxl = []
with open(sys.argv[1], 'r') as f:
  for l in f:
    l=l.strip()
    l = [int(c) for c in l.split(',')]
    pxl.append(l)

pxl.sort(key=functools.cmp_to_key(compare))
print(pxl)

start = 0
stop = 0

def minmax(l):
    mi = copy.deepcopy(l[0])
    ma = copy.deepcopy(l[0])
    for e in l:
        print(e)
        for i in range(3):
            if e[i] > ma[i]:
                print('update')
                ma[i] = e[i]
            if e[i] < mi[i]:
                print('update')
                mi[i] = e[i]
        print(mi)
        print(ma)

    return mi,ma


mi, ma = minmax(pxl)
for i in range(3):
    mi[i] -= 2
    ma[i] += 2
print(mi)
print(ma)
prevm = None
prevpxl = []
m = None
cnt = 0
while stop < len(pxl) > 0:
    while stop < len(pxl) and  pxl[stop][0] == pxl[start][0]:
        stop+=1
    print(pxl[start:stop])
    prevm = m
    m=np.zeros((ma[1]-mi[1],ma[2]-mi[2]))
    p = pxl[start:stop]
    if prevm is not None:
        print(f'shape {prevm.shape}')
        print(f'{prevm[1][1]}')
    for pp in p:
        m[pp[1],pp[2]] = 1
    print (m)
    for pp in p:
        x = pp[0]
        y = pp[1]
        z = pp[2]
        if prevm is not None:
            if prevm[y][z] == 0:
                cnt+=1
        else:
            cnt+=1
        if m[y,z+1] == 0:
            cnt+=1
        if m[y,z-1] == 0:
            cnt+=1
        if m[y+1,z] == 0:
            cnt+=1
        if m[y-1,z] == 0:
            cnt+=1
        print (f' test {pp} {cnt}')

    for pp in prevpxl:
        x = pp[0]
        y = pp[1]
        z = pp[2]
        if m[y,z] == 0:
            cnt+=1
        print (f' prev test {pp} {cnt}')
    print(f'cnt {cnt}')
    prevm =m
    prevpxl =p
    start = stop
    stop+=1

cnt+= np.sum(prevm)
print(cnt)
