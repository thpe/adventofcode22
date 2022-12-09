#!/usr/bin/env python3
import sys
import numpy as np
import re



r = 0
c = 0

m = []
with open(sys.argv[1], 'r') as f:
  for l in f:
    m.append([])
    for c in l.strip():
        m[r].append(int(c))
    r += 1

m = np.array(m)

v = np.zeros(m.shape)
c = m.shape[1]

for ir in range(r):
    v[ir][0] = 1
    href = m[ir][0]
    hmax = m[ir][0]
    for ic in range(1,c):
        h = m[ir][ic]
        if h <= hmax:
            continue
        v[ir][ic] = 1
        hmax = max(h, hmax)
    v[ir][c-1] = 1
    href = m[ir][c-1]
    hmax = m[ir][c-1]
    for ic in range(c-2,0,-1):
        h = m[ir][ic]
        if h <= hmax:
            continue
        v[ir][ic] = 1
        hmax = max(h, hmax)


for ic in range(c):
    v[0][ic] = 1
    href = m[0][ic]
    hmax = m[0][ic]
    for ir in range(1,r):
        h = m[ir][ic]
        if h <= hmax:
            continue
        v[ir][ic] = 1
        hmax = max(h, hmax)
    v[r-1][ic] = 1
    href = m[r-1][ic]
    hmax = m[r-1][ic]
    for ir in range(r-2,0,-1):
        h = m[ir][ic]
        if h <= hmax:
            continue
        v[ir][ic] = 1
        hmax = max(h, hmax)
print(v.sum())
