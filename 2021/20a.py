from collections import defaultdict
import sys
from icecream import ic
import re

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline()):
        lines.append(line.rstrip())
iea = lines[0]
iea2 = ""
for c in iea:
    if c == '#':
        iea2 += '.'
    else:
        iea2 += '#'
iea2 = iea

d = defaultdict(bool)

for i in range(2, len(lines)):
    for j,c in enumerate(lines[i]):
        d[(j,i-2)] = ( c == "#" )

d['miny'] = 0
d['minx'] = 0
d['maxy'] = len(lines) - 2
d['maxx'] = len(lines[2])

def inclusive_range(one, two):
    if one <= two:
        return range(one, two+1, 1)
    else:
        return range(one, two-1, -1)

def xform(d, p, iea, i):
    rs = ""
    for y in inclusive_range(p[1]-1, p[1]+1):
        for x in inclusive_range(p[0]-1, p[0]+1):
            rs += str(int(d[(x,y)]))
    if i % 2:
        return (iea[int(rs,2)] != "#")
    else:
        return (iea[int(rs,2)] == "#")

def findminy(d):
    miny = 0
    for p in d.keys():
        if p[1] < miny:
            miny = p[1]
    return miny

def findmaxy(d):
    maxy = 0
    for p in d.keys():
        if p[1] > maxy:
            maxy = p[1]
    return maxy

def findminx(d):
    minx = 0
    for p in d.keys():
        if p[0] < minx:
            minx = p[0]
    return minx

def findmaxx(d):
    maxx = 0
    for p in d.keys():
        if p[0] > maxx:
            maxx = p[0]
    return maxx

def printD(d):
    for y in inclusive_range(d['miny'], d['maxy']):
        line = ""
        for x in inclusive_range(d['minx'], d['maxx']):
            if d[(x,y)]:
                line += "#"
            else:
                line += "."
        print(line)

printD(d)
 
for i in inclusive_range(1,2):
    nd = defaultdict(bool)
    for y in inclusive_range(d['miny'] - 4, d['maxy'] + 4):
        for x in inclusive_range(d['minx'] - 4, d['maxx'] + 4):
            nd[(x,y)] = xform(d, (x,y), iea, i)
    nd['miny'] = d['miny'] - 1
    nd['maxy'] = d['maxy'] + 1
    nd['minx'] = d['minx'] - 1
    nd['maxx'] = d['maxx'] + 1 
    ndc = nd.copy()
    for p in ndc.keys():
        if isinstance(p,tuple):
            if p[0] < nd['minx'] or p[0]>nd['maxx'] or p[1]<nd['miny'] or p[1]>nd['maxy']:
                del nd[p]
    d = nd.copy()
    printD(d)

ic(sum(int(x) for x in d.values() if isinstance(x,bool)))
#ic(d)
