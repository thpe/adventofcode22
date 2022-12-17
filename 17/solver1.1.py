#!/usr/bin/env python3
import sys
import numpy as np
import re
import copy
from tqdm import tqdm


block = [
np.array([[1,1,1,1]]),
np.array([[0,1,0],
          [1,1,1],
          [0,1,0]]),
np.array([[1,1,1],
          [0,0,1],
          [0,0,1]]),
np.array([[1],
          [1],
          [1],
          [1]]),
np.array([[1,1],
          [1,1]])
]

m = np.zeros((100000,7))
profile = np.zeros(7)

np.set_printoptions(threshold=sys.maxsize,linewidth=2000)

seq = []
with open(sys.argv[1], 'r') as f:
  for l in f:
    l=l.strip()
    l = [(ord(c) - ord('>') + 1) for c in [*l]]
    seq=l

def start_height(m):
    cnt=0
    for i in range(m.shape[0]):
        if np.max(m[i]) > 0:
            cnt+=1
        else:
            break
    return cnt+3

def check(pos, block, m):
    if pos[0] < 0 or pos[1] < 0 or pos[1]+block.shape[1]-1 >= m.shape[1]:
        return False
#        print(f'oob+ {pos}')
    for y in range(block.shape[0]):
        my = pos[0]+y
        for x in range(block.shape[1]):
            mx = pos[1]+x
            if block[y][x] > 0 and m[my][mx] > 0:
                return False
    return True

def register(pos, block, m):
#    print(f'register {pos} {block}')
    for y in range(block.shape[0]):
        my = pos[0]+y
        for x in range(block.shape[1]):
            mx = pos[1]+x
            if block[y][x] > 0:
                m[my][mx] = 1
    return True

def fall_object(p,b,seq):
    pos = [start_height(p),2]

#    print(f'{b}')
    while True:
        s = seq.pop(0)
        seq.append(s)

        pos[1] += s
        if not check(pos, b,p):
            pos[1] -= s
#            print(f'adjust 0')
#        else:
#            print(f'adjust {s}')

        pos[0] -= 1

#        print(f'test {pos}')
        if not check(pos, b,p):
            pos[0] += 1
            register(pos,b,p)
            break



lut = {}
def sequence(p, seq):
    hacc = 0
    mm = 1000000000000
    pbar = tqdm(total=mm)
    i = 0
    while i < mm:
        oh = start_height(m)-3
        fall_object(m,block[i%5],seq)
#        print(seq)
        cnt = 0
#        print(start_height(m)-3)
#        if i%5 == 0 and i >10 and hacc == 0:
        if i >10 and hacc == 0:
            h = hash(i%5)+hash(tuple(p[i-10:i].flatten())) + hash(tuple(seq))
            if h not in lut:
                lut[h] = [i, start_height(m)-3]
            else:
                sh = start_height(m)-3

                cycle = i-lut[h][0]
                add = sh-lut[h][1]
                print(f'found {i} {lut[h]} diff {i-lut[h][0]} {sh-lut[h][1]}')
#                lut[h] = [i, start_height(m)-3]
                cnt = int((mm - i) / cycle)
                i+= cnt * cycle
                pbar.update(cnt*cycle)
                hacc+= cnt*add

        i+=1
        pbar.update(1)
    pbar.close()
    return hacc
#for i in range(2):
#    print(f'round {i} ##################################3')
hacc = sequence(m, seq)
for r in range(40,-1,-1):
    print('|',end='')
    for c in range(7):
        if m[r][c] > 0:
            print('#', end='')
        else:
            print('.',end='')
    print('|')
print(start_height(m)-3 +hacc)
