#!/usr/bin/env python3
import sys
import numpy as np
import re
import copy



np.set_printoptions(threshold=sys.maxsize,linewidth=2000)

segments = []

with open(sys.argv[1], 'r') as f:
  for l in f:
    l=l.strip()
    l = l.split(' -> ')
    l = [np.array([int(x[0]),int(x[1])]) for x in [x.split(',') for x in l]]
    segments.append(l)



start = [500,0]
mi = start
ma = start

for i in range(len(segments)):
    for j in range(len(segments[i])):
        e = segments[i][j]
        mi = [min(e[0],mi[0]),min(e[1],mi[1])]
        ma = [max(e[0],ma[0]),max(e[1],ma[1])]

off = int(mi[0]-ma[1])
offa= np.array([off,0])
m = np.zeros(((ma[0] -mi[0]+3)*5, ma[1]+3),int)
for i in range(m.shape[0]):
    m[i,-1] = 1
start-=offa

for s in segments:
    ss = s[0] -offa
    for e in s[1:]:
        e -= offa
        d = np.abs(ss - e).astype(int)
        if d[0] != 0:
            for x in range(d[0]+1):
                x = x + min(ss[0], e[0])
                m[x,e[1]] = 1
        elif d[1] != 0:
            for y in range(d[1]+1):
                y += min(ss[1], e[1])
                m[e[0],y] = 1
        ss = e

cnt = 0
sol1found = False
def movesand(m,spos, found):
    if spos[1] >= m.shape[1]-2 and not found:
        print (f'solution1 {cnt}')
        found = True
    if m[spos[0],spos[1]] != 0:
        raise Exception('array full')
    n = spos + [0,1]
    if m[n[0],n[1]] == 0:
        m,found = movesand(m,n, found)
    else:
        n = spos + [-1,1]
        if m[n[0],n[1]] == 0:
            m,found = movesand(m,n, found)
        else:
            n = spos + [1,1]
            if m[n[0],n[1]] == 0:
                m,found = movesand(m,n, found)
            else:
                m[spos[0],spos[1]] = 2
    return m,found

while True:
    try:
        m, sol1found = movesand(m,start,sol1found)
    except Exception as e:
       print(f'finished {e}')
       break
#    print(m.T)
#    print(cnt)
    cnt+=1
print(m.T)
print(cnt)

