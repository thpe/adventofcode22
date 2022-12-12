#!/usr/bin/env python3
import sys
import numpy as np
import re


noop = re.compile(r'(noop)')
addx = re.compile(r'addx (-?\d+)')

x = 1
pcnt = 0

xx = []
xxx = []

crty = 0
crtxo = -1

def check(pcnt, crty):
    if (pcnt - 20) % 40 == 0:
        xx.append(x)
        xxx.append(x*pcnt)
        crty += 1
    return crty


crt = np.zeros([7,40])

def crtdraw(crtxo, xxx):
    crtx = (pcnt) % 40
    if (abs(crtx - x) <= 1):
        crt[crty][crtx] = 1
    if crtxo < 1:
        crtxo += 1
    return crtxo
with open(sys.argv[1], 'r') as f:
  for l in f:
    l = l.strip()
    m = noop.match(l)
    if m is not None:
        pcnt+=1
        crtxo = crtdraw(crtxo,x)
        crty = check(pcnt, crty)
    else:
        m = addx.match(l)
        if m is not None:
            v = int(m.group(1))
            crtxo = crtdraw(crtxo,x)
            pcnt+=1
            crty = check(pcnt, crty)
            crtxo = crtdraw(crtxo,x)
            pcnt+=1
            crty = check(pcnt, crty)
            x += v
            crtxo = crtdraw(crtxo,x)
            crtxo = -1
print(f'solution 1 {sum(xxx)}')
for r in range(crt.shape[0]):
    for c in range(crt.shape[1]):
        v = crt[r][c]
        if v == 1:
            print('#', end='')
        else:
            print('.', end='')
    print('')
