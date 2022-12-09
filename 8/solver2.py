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

tscore = np.zeros(m.shape)
c = m.shape[1]


cmax = 0
rmax = 0
hmax = 0
for rref in range(1,r):
    for cref in range(1,c):
        href = m[rref][cref]
        score = np.zeros(4)
        ir = rref
        for ic in range(cref+1,c):
            h = m[ir][ic]
            score[0] += 1
            if h >= href:
                break
        for ic in range(cref-1,-1,-1):
            h = m[ir][ic]
            score[1] += 1
            if h >= href:
                break
        ic = cref
        for ir in range(rref+1,r):
            h = m[ir][ic]
            score[2] += 1
            if h >= href:
                break
        for ir in range(rref-1,-1,-1):
            h = m[ir][ic]
            score[3] += 1
            if h >= href:
                break
        tscore[rref][cref] = score[0] * score[1] * score[2] * score[3]
        if tscore[rref][cref] > hmax:
            hmax = tscore[rref][cref]
            rmax = rref
            cmax = cref
print(tscore.max())

