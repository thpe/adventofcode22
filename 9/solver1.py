#!/usr/bin/env python3
import sys
import numpy as np
import re

prog = re.compile(r'([UDLR]) (\d+)')

r = 0
c = 0

m = []
pos = [np.array([0,0]) for i in range(10)]
move = {'U': np.array([1,0]),
        'D': np.array([-1,0]),
        'R': np.array([0,1]),
        'L': np.array([0,-1])}

vis = {}
vis1 = {}
with open(sys.argv[1], 'r') as f:
  for l in f:
    r = prog.match(l)
    for i in range(int(r.group(2))):
        pos[0] += move[r.group(1)]
        for j in range(1,10):
            diff = pos[j-1] - pos[j]
            if np.linalg.norm(diff) >= 2:
                m = np.array([0,0])
                if abs(diff[0]) > 0:
                    m += np.array([int(diff[0] / abs(diff[0])), 0])
                if abs(diff[1]) > 0:
                    m += np.array([0, int(diff[1] / abs(diff[1]))])
                pos[j] += m
                if j==1:
                    vis1[f'{pos[1][0]},{pos[1][1]}'] =1
                if j==9:
                    vis[f'{pos[9][0]},{pos[9][1]}'] =1
            diff = pos[j-1] - pos[j]


print(sum(vis1.values())+1)
print(sum(vis.values())+1)
#print(vis)
