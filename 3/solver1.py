#!/usr/bin/env python3


import sys
import numpy as np

def pri (c):
    prio = ord(c) - ord('a') + 1
    if (prio > 26 or prio < 0):
        prio = ord(c) - ord('A') + 27
    return prio

count = 0
with open(sys.argv[1], 'r') as f:
  for l in f:
    a = np.zeros(2*26+1)
    l = l.strip()
    n = len(l)
    for c in range(int(n/2)):
      prio = pri(l[c])
      a[prio] += 1

    for u in range(int(n/2)):
      c = u + int(n/2)
      prio = pri(l[c])
      if (a[prio] > 0):
        count += prio
        break

print (count)
