#This takes 4 hours to run :(

from collections import defaultdict
import sys
from icecream import ic

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)
ic(lines)
od = {}
unvisited = set()
od['maxx'] = len(lines[0])
od['maxy'] = len(lines)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        od[(x,y)] = int(c)
        unvisited.add((x,y))
ic(od)

def funnyAdd(a,b):
    c = a + b
    if c > 9:
        c = ( c % 10 ) + 1
    return c

d = {}
for by in range(5):
    for bx in range(5):
        for p in od.keys():
            if not isinstance(p, str):
                #ic(p)
                #ic((p[0]+(bx*od['maxx']),p[1]+(by*od['maxy'])))
                d[(p[0]+(bx*od['maxx']),p[1]+(by*od['maxy']))] = funnyAdd(od[p],by+bx)
                unvisited.add((p[0]+(bx*od['maxx']),p[1]+(by*od['maxy'])))
d['maxx'] = od['maxx'] * 5
d['maxy'] = od['maxy'] * 5


e = {}
for k in d.keys():
    if not isinstance(k, str):
        e[k] = float("inf")
    else:
        e[k] = d[k]
e[(0,0)] = 0
ic(e)

def drawBoard(d):
    for y in range(d['maxy']):
        nl = ""
        for x in range(d['maxx']):
            if isinstance(d[(x,y)],float):
                nl += "x"
            else:
                nl += str(d[(x,y)])
        print(nl)

drawBoard(d)

def un(p):
    return e[p]

node = (0,0)
while node != (d['maxx'] - 1, d['maxy'] - 1):
    unvisited.remove(node)
    for p in [(node[0]-1,node[1]),(node[0]+1,node[1]),(node[0],node[1]-1),(node[0],node[1]+1)]:
        if p in d.keys() and p in unvisited:
    #        ic(p)
            if e[node] + d[p] < e[p]:
                e[p] = e[node] + d[p]
    #drawBoard(e)
    nextNode = min((p for p in e if p in unvisited), key=un)
    #ic(nextNode)
    node = nextNode

ic(e[(d['maxx'] - 1, d['maxy'] - 1)])
