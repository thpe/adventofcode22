#!/usr/bin/env python3


import sys

count = 0
m = []
with open(sys.argv[1], 'r') as f:
  for l in f:
    if len(l) > 1:
        i = int(l)
        count += i
    else:
        m.append(count)
        count = 0


m.sort()
print("solution 1")
print(m[-1])
print("solution 2")

print(m[-1]+m[-2]+m[-3])


