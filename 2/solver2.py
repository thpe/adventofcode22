#!/usr/bin/env python3


import sys

count = 0
with open(sys.argv[1], 'r') as f:
  for l in f:
    if len(l) > 1:
      a = ord(l[0]) - ord('A')
      b = ord(l[2]) - ord('X')

      res = a + b - 1
      b = res % 3
      res = b - a
      res = res % 3
      score = b+1
      if (res == 0):
        score += 3
      if (res == 1):
        score += 6
      print(f'{l[0]} {a} -> {l[2]} {b}: res {res} score {score}')
      count += score

print (count)
