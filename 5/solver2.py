#!/usr/bin/env python3


import sys
import numpy as np
import re

def move(r, stack):
    temp = []
    for i in range(r[0]):
        temp.append(stack[r[1]].pop())

    for i in range(len(temp)):
        stack[r[2]].append(temp.pop())
    return stack

stack = [[] for i in range(10)]
count = 0
progstack = re.compile(".(.)...(.)...(.)...(.)...(.)...(.)...(.)...(.)...(.)")
prog = re.compile("move ([0-9]+) from ([0-9]+) to ([0-9]+)")
with open(sys.argv[1], 'r') as f:
  for l in f:
    res = progstack.match(l)
    if res is None:
        break
    for i in range(1,10):
        if res.group(i) != ' ':
            stack[i].append(res.group(i))

for i in range(10):
    stack[i].reverse()
with open(sys.argv[1], 'r') as f:
  for l in f:
    res = prog.match(l)
    if res is None:
        continue
    r = [int(res.group(i)) for i in range(1,4)]
    stack= move(r, stack)

last = [stack[i][-1] for i in range(1,10)]
print(''.join(last))
