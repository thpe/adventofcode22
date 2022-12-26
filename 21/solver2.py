#!/usr/bin/env python3
import sys
import numpy as np
import re
import copy
from tqdm import tqdm
import functools

def compare(a,b):
    idx = 0
    if a[idx] < b[idx]:
        return -1
    elif a[idx] > b[idx]:
        return 1
    else:
        return 0

prog1 = re.compile(r'([a-z]{4}): (\d+)')
prog2 = re.compile(r'([a-z]{4}): ([a-z]{4}) (.) ([a-z]{4})')

np.set_printoptions(threshold=sys.maxsize,linewidth=2000)

tree = {}
with open(sys.argv[1], 'r') as f:
  for l in f:
    l=l.strip()
    res = prog1.match(l)
    if res is not None:
        tree[res.group(1)] = [int(res.group(2))]
    else:
        res = prog2.match(l)
        tree[res.group(1)] = [res.group(2), res.group(3), res.group(4)]



def solve(t,n):
    if n == 'humn':
        return None
    if len(t[n]) == 1:
        return t[n][0]

    l = solve(t,t[n][0])
    r = solve(t,t[n][2])

    if t[n][1] == '+':
        return l+r
    if t[n][1] == '-':
        return l-r
    if t[n][1] == '*':
        return l*r
    if t[n][1] == '/':
        return l/r

def compute(t,n,v):
    if n == 'humn':
        return v
    if len(t[n]) == 1:
        return t[n][0]

    l=0
    r=0
    try:
        l = solve(t,t[n][0])
    except:
        l =None
    try:
        r = solve(t,t[n][2])
    except:
        r=None
    if t[n][1] == '+':
        if l is None:
            return compute(t,t[n][0],v-r)
        else:
            return compute(t,t[n][2],v-l)
    if t[n][1] == '-':
        if l is None:
            return compute(t,t[n][0],v+r)
        else:
            return compute(t,t[n][2],l-v)
    if t[n][1] == '*':
        if l is None:
            return compute(t,t[n][0],v/r)
        else:
            return compute(t,t[n][2],v/l)
    if t[n][1] == '/':
        if l is None:
            return compute(t,t[n][0],v*r)
        else:
            return compute(t,t[n][2],l/v)

def solveroot(t,n):
    if len(t[n]) == 1:
        return t[n][0]

    l=0
    r=0
    try:
        l = solve(t,t[n][0])
    except:
        l =None
    try:
        r = solve(t,t[n][2])
    except:
        r=None

    if l is None:
        return compute(t,t[n][0],r)
    else:
        return compute(t,t[n][2],l)
print(solveroot(tree,'root'))
