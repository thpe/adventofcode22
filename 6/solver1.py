#!/usr/bin/env python3


import sys
import numpy as np
import re

n = 14 # use n=4 for first solution

with open(sys.argv[1], 'r') as f:
  for l in f:
    l = [*l.strip()]
    for i in range(n,len(l)):
        a = np.zeros(26)
        for j in range(n+1):
            if j == n:
                print(f'pos {i+1}')
                print(l[i-n+1:i+1])
            c = ord(l[i-j]) - ord('a')
            if a[c] == 0:
                a[c] += 1
            else:
                break

