#!/usr/bin/env python3
import sys
import numpy as np
import re
import copy



np.set_printoptions(threshold=sys.maxsize,linewidth=2000)

prog = re.compile(r'Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.*)')
segments = []

adjunct = {}

with open(sys.argv[1], 'r') as f:
  for l in f:
    l=l.strip()
    r = prog.match(l)
    print(r.groups())
    adjunct[r.group(1)] = [int(r.group(2)),r.group(3).split(', '),False]

print(adjunct)

def flow(adjunct, pos):
    if isopenv(adjunct, pos):
        return 0
    return adjunct[pos][0]

def isopenv(adjunct, pos):
    return adjunct[pos][2]
def isallopenv(adjunct):
    for k,v in adjunct.items():
        if (not v[2]) and v[0] > 0 :
            return False
    return True

def printallopen(adjunct):
    o = []
    for k,v in adjunct.items():
        if v[2]:
           o.append(k)
    print(f'  open valves {o}')

def openv(a, pos):
    print(f'  open {pos} {flow(a, pos)}')
    a[pos][2] = True
    return a
def closev(a, pos):
#    print(f'  close {pos} {flow(a, pos)}')
    a[pos][2] = False
    return a

cadjunct = {}

def bfs(adjunct, pos, visited, d):
    d += 1
    todo = []
    for n in adjunct[pos][1]:
        if not n in visited.keys():
            visited[n] = d
            todo.append(n)

    print(f'fill root {pos} {todo} {visited}')
    ntodo = []
    while len(todo) > 0:
        print(f'{todo} {visited}')
        d += 1
        for r in todo:
            for n in adjunct[r][1]:
                if not n in visited.keys():
                    visited[n] = d
                    ntodo.append(n)

        todo = ntodo
        ntodo = []

    return visited

def clean(adjunct):
    cadjunct = {}
    poplist = []
    for k,v in adjunct.items():
        nn = bfs(adjunct, k, {k: 0}, 0)
        if flow(adjunct, k) > 0 or k == 'AA':
            cadjunct[k] = [adjunct[k][0], nn,False]
        else:
            poplist.append(k)

    print(f'poplist {poplist}')
    for k,v in cadjunct.items():
        if k in cadjunct[k][1].keys():
            cadjunct[k][1].pop(k)
        for e in poplist:
            if e in cadjunct[k][1].keys():
                cadjunct[k][1].pop(e)
    return cadjunct

def solve(adjunct, pos, cflow, tflow, time, history):
    print(f'visit {pos} {time} cflow {cflow} {history}')
    printallopen(adjunct)
    if time >= 30:
        print('time out')
        return adjunct, pos, cflow, tflow

#    tflow+= cflow
    lflow = flow(adjunct,pos)
    openwait = 0
    if lflow > 0:
        openv(adjunct, pos)
        openwait = 1
        history.append((pos,time))
    if isallopenv(adjunct):
        print(f'all open ############# {history}')
        if history[-1][0] == pos:
            history.pop()
        closev(adjunct, pos)
        return adjunct, pos, cflow, tflow+(30-time)*(lflow+cflow) +cflow
    mtflow = tflow
    for n,v in adjunct[pos][1].items():
#        print(f'    check {pos} -> {n}')
        if flow(adjunct, n) == 0:
#            print(f'      no flow')
            continue
        if time + v > 30:
#            print(f'      no time')
            continue
#        print(f'test {n} dist {v} flow {flow(adjunct, n)}')
        r, p, c, t = solve(adjunct, n, cflow+lflow, tflow+cflow*openwait+(cflow+lflow)*v, time+1*openwait+v, history)
        if t > mtflow:
            mtflow = t
            print(f'  new optimum1 {mtflow} {history}')
    closev(adjunct, pos)
    tflow = mtflow


    waitflow= tflow+(30-time)*cflow
    if waitflow > mtflow:
        print(f'  new optimum2 {mtflow} {history}')
        tflow = mtflow


#    mtflow = tflow
#    for n,v in adjunct[pos][1].items():
#        r, p, c, t = solve(adjunct, n, cflow, tflow+cflow, time+v)
#        if t > mtflow:
#            mtflow = t
#            print(f'new optimum2 {tflow}')
#
#    tflow = mtflow


    if len(history) > 0 and history[-1][0] == pos:
        history.pop()
    return adjunct, pos, cflow, tflow



cadjunct = clean(adjunct)
print(cadjunct)

r, p, c, t = solve(cadjunct, 'AA', 0, 0, 1, [])
print(f'result {t}')
