#!/usr/bin/env python3


import sys
import numpy as np

def pri (c):
    prio = ord(c) - ord('a') + 1
    if (prio > 26 or prio < 0):
        prio = ord(c) - ord('A') + 27
    return prio

count = 0
ff = []
with open(sys.argv[1], 'r') as f:
  for l in f:
    ff.append(l)
  for idx in range(0,len(ff), 3):
    l1 = ff[idx]
    l2 = ff[idx+1]
    l3 = ff[idx+2]
    a1 = np.zeros(2*26+1)
    a2 = np.zeros(2*26+1)
    a3 = np.zeros(2*26+1)
    l = l1.strip()
    n = len(l)
    for c in range(n):
      prio = pri(l[c])
      a1[prio] += 1
    l = l2.strip()
    n = len(l)
    for c in range(n):
      prio = pri(l[c])
      a2[prio] += 1
    l = l3.strip()
    n = len(l)
    for c in range(n):
      prio = pri(l[c])
      a3[prio] += 1

    for u in range(a1.shape[0]):
      if a1[u] > 0 and a2[u] > 0 and a3[u] > 0:
        print (f'found {u} {a1[u]} {a2[u]} {a3[u]}')
        count += u
        break

print (count)
