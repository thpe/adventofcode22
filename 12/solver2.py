#!/usr/bin/env python3
import sys
import numpy as np
import re



rows = 0
cols = 0

start = None
end = None

m = []
with open(sys.argv[1], 'r') as f:
  for l in f:
    m.append([])
    cols = 0
    for c in l.strip():
        if c == 'S':
            start = (rows,cols)
            print(f'start {start}')
            c = 'a'
        if c == 'E':
            end = (rows,cols)
            print(f'end {end}')
            c = 'z'
        m[rows].append(ord(c) - ord('a'))
        cols += 1
    rows += 1

m = np.array(m)

print (m)


l = [np.array(end)]

h=0
mm = 1e10
d = mm * np.ones(m.shape)
dist = 0
d[start] = 0

def neighbours(p, h):
    r = []
    if p[0] > 0:
        pp = p-(1,0)
        if d[pp[0], pp[1]] == mm:
            if (m[pp[0], pp[1]] - h) > -2 :
                r.append(pp)
    if p[0] < rows-1:
        pp = p+(1,0)
        if d[pp[0], pp[1]] == mm:
            if (m[pp[0], pp[1]] - h) > -2 :
                r.append(pp)
    if p[1] > 0:
        pp = p-(0,1)
        if d[pp[0], pp[1]] == mm:
            if (m[pp[0], pp[1]] - h) > -2 :
                r.append(pp)
    if p[1] < cols-1:
        pp = p+(0,1)
        if d[pp[0], pp[1]] == mm:
            if (m[pp[0], pp[1]] - h) > -2 :
                r.append(pp)

    return r
finished = False
low = []
while not finished and len(l) > 0:
    dist += 1
    ll = []
    while len(l) > 0:
        p = l.pop(0)
        h = m[p[0],p[1]]
        print(f'{p} {dist} {len(l)}')
        if h == 0:
            low.append(p)
            finished = True
        for n in neighbours(p, h):
            d[n[0], n[1]] = dist
            ll.append(n)

    l = ll

print(d[end])
print(low)
print(d[low[0][0], low[0][1]])
