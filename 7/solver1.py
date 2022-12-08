#!/usr/bin/env python3
import sys
import numpy as np
import re

cdcmd = re.compile(r'\$ cd (.*)')

lscmd = re.compile(r'\$ ls')
fileinfo = re.compile(r'([0-9]*) (\S)')
dirinfo = re.compile(r'dir (\S)')


def addsmall(size, ss):
    if size < 100000:
        return size + ss
    return ss

def traverse(path, d, cmdlist, ss):
    path.append(d)
    size = 0
    completed = True
    dirs = []
    vdirs = []
    while len(cmdlist) > 0:
        cc = cmdlist.pop(0)
        r = cdcmd.match(cc)
        if r is not None:
            dd = r.group(1)
            if dd == '/' and len(path) > 1:
                ss = addsmall(size, ss)
                path.pop()
                return size, True, ss
            if dd == '..':
                ss = addsmall(size, ss)
                path.pop()
                return size, False, ss
            vdirs.append(dd)
            rr, dst, sss = traverse (path, r.group(1), cmdlist, ss)
            ss = sss
            if rr != -1:
                size+= rr
            if dst:
                if completed:
                    ss = addsmall(size, ss)
                    path.pop()
                    return size, True, ss
                else:
                    ss = addsmall(size, ss)
                    path.pop()
                    return -1, True, ss

        r = lscmd.match(cc)
        if r is not None:
            while len(cmdlist) > 0:
                ccc = cmdlist.pop(0)
                r = fileinfo.match(ccc)
                if r is not None:
                    size+= int(r.group(1))
                else:
                    r = dirinfo.match(ccc)
                    if r is not None:
                        dirs.append(r.group(1))
                    else:
                        cmdlist.insert(0, ccc)
                        break;
    ss = addsmall(size, ss)
    return size, True, ss

c = []

with open(sys.argv[1], 'r') as f:
  for l in f:
    c.append(l.strip())


p = []
d = '/'
rr, dst, ss = traverse(p, d, c, 0)
print(ss)
