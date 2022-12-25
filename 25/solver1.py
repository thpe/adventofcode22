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


np.set_printoptions(threshold=sys.maxsize,linewidth=2000)


bp = []

lut = {
'2':2,
'1':1,
'0':0,
'-':-1,
'=':-2
}
rlut = {
2:'2',
1:'1',
0:'0',
-1:'-',
-2:'='
}
num = 0
with open(sys.argv[1], 'r') as f:
  for l in f:
    l=l.strip()
    l = [*l]
    l.reverse()
    n = 0
    for i in range (len(l)):
        n+= pow(5,i)*lut[l[i]]

    num+=n
print(num)

m = int(np.log(num)/np.log(5))+1
rem = num
fac = []
for i in reversed(range(m)):
    mi = num
    best = 0
    for j in range(-2,3):
        s = pow(5,i)*j
        if mi > abs(rem-s):
            best = j
            mi = abs(rem-s)
    fac.append(rlut[best])
    rem = rem - best * pow(5,i)

print("".join(fac))

