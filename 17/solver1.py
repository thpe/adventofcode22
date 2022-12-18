#!/usr/bin/env python3
import sys
import numpy as np
import re
import copy


profile = np.zeros(7)

np.set_printoptions(threshold=sys.maxsize,linewidth=2000)

seq = []
with open(sys.argv[1], 'r') as f:
  for l in f:
    l=l.strip()
    l = [(ord(c) - ord('>') + 1) for c in [*l]]
    print (l)
    seq=l

def start_height(p):
    return np.max(p)+4

def fall_object(p,w,h,seq,cross=False,lshape=False):
    pos = [2, start_height(p)]

    lcorr = np.zeros(4)
    hcorr = np.zeros(4)
    if cross:
        lcorr = np.array([-1,0,-1,0])
        hcorr = lcorr
    if lshape:
        hcorr = np.array([-2,-2,0,0])
    cleft = p.shape[0]
    cright = -1
    while True:
        s = seq.pop(0)
        seq.append(s)
        if s == -1:
            pos[0] = max(cright+1, pos[0]+s)
            print('left')
        if s == 1:
            pos[0] = min(cleft-w, pos[0]+s)
            print('right')

        pos[1] -= 1
        collision = False
        for i in range(pos[0], pos[0]+w):
            if p[i] >= pos[1] - lcorr[i-pos[0]]:
                print(f'collision at {i} ({i-pos[0]}) {pos} {lcorr} {p}')
                collision = True
#            else:
#                print(f'     free at {i} ({i-pos[0]}) {pos} {lcorr} {p}')

        if collision:
            pos[1] += 0
            for i in range(pos[0], pos[0]+w):
                p[i] = pos[1]+h + hcorr[i-pos[0]]
            break
        for i in range(pos[0]-1,cright,-1):
            if p[i] >= pos[1]:
                cright=i
                print(f'move cright {cright}')
                break
        for i in range(pos[0]+w,cleft):
#            print(f'check cleft {pos} {p} {cleft}')
            if p[i] >= pos[1]:
                cleft=i
#                print(f'move cleft {cleft}')
                break


def fall_square(p, seq):
    w = 2
    h = 2
    fall_object(p,w,h,seq)
def fall_vert(p, seq):
    w = 1
    h = 4
    fall_object(p,w,h,seq)

def fall_hori(p, seq):
    w = 4
    h = 1
    fall_object(p,w,h,seq)
def fall_cross(p, seq):
    w = 3
    h = 3
    fall_object(p,w,h,seq, True)
def fall_L(p, seq):
    w = 3
    h = 3
    fall_object(p,w,h,seq, False,True)


def sequence(p, seq):
    fall_hori(p,seq)
    print(p)
    fall_cross(p,seq)
    print(p)
    fall_L(p,seq)
    print(p)
    fall_vert(p,seq)
    print(p)
    fall_square(p, seq)
    print(p)
for i in range(2):
    print(f'round {i} ##################################3')
    sequence(profile, seq)
