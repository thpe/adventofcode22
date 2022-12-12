#!/usr/bin/env python3
import sys
import numpy as np
import re
from tqdm import tqdm

monk = []

class Monkey:
    def __init__(self):
        self.items = []
        self.a = [0,0,0]
        self.insp = 0
    def op (self, i):
        return self.a[2] * i * i + self.a[1] * i + self.a[0]
    def run(self):
        for i in range(len(self.items)):
            i = self.items.pop(0)
#            print(f'{self.id} op {self.a} {i} {self.op(i)}')
            i = self.op(i)
            self.throw(i)
            self.insp += 1


    def throw(self, i):
        t = self.ftarget
        i = int(i / 3)
#        print(f'{self.id} {self.items} throws {i} to {t}')
        if i % self.divisible == 0:
            t = self.ttarget
        #    i = int(i / self.divisible)
        monk[t].items.append(i)
#        print(f'{self.id} {self.divisible} {self.items} throws {i} to {t}')


sitem = re.compile(r'Starting items: (.*)')
op    = re.compile('Operation: new = (\S+) ([\*\+]) (\S+)')
dtest = re.compile(r'Test: divisible by (\d+)')
ttarget = re.compile(r'If true: throw to monkey (\d+)')
ftarget = re.compile(r'If false: throw to monkey (\d+)')



with open(sys.argv[1], 'r') as f:
  for l in f:
    l = l.strip()
    #print(l)
    r=sitem.match(l)
    if r is not None:
        monk.append(Monkey())
        li = r.group(1)
        li = li.split(', ')
        li = [int(lii) for lii in li]
        monk[-1].items = li
        monk[-1].id = len(monk) -1
        #print(li)
        continue
    r=op.match(l)
    if r is not None:
        #print(r.groups())
        if r.group(2) == '+':
            monk[-1].a[1] = 1
            monk[-1].a[0] = int(r.group(3))
        elif r.group(2) == '*':
            if r.group(3) == 'old':
                monk[-1].a[2] = 1 ## removed
                monk[-1].a[1] = 0 ## removed
            else:
                monk[-1].a[1] = int(r.group(3))
        #print(monk[-1].a)
    r=dtest.match(l)
    if r is not None:
        v = int(r.group(1))
        #print(f'div {v}')
        monk[-1].divisible = int(r.group(1))

    r=ttarget.match(l)
    if r is not None:
        v = int(r.group(1))
        #print(f'ttarget {v}')
        monk[-1].ttarget = v
    r=ftarget.match(l)
    if r is not None:
        v = int(r.group(1))
        #print(f'ftarget {v}')
        monk[-1].ftarget = v

pr = [1,20,1000,2000,3000,4000,5000,6000,7000,8000,9000]

for m in monk:
    di = []
    for i in m.items:
        d = {}
        for mm in monk:
            d[mm.id] = i % mm.divisible
for i in tqdm(range(20)):
    for m in monk:
        m.run()
    if i in pr:
        ii = [m.insp for m in monk]
        print(ii)


ii = []
for m in monk:
    ii.append(m.insp)
ii.sort()
print(ii)
print(ii[-2] * ii[-1])

