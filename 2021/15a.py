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
d = {}
unvisited = set()
d['maxx'] = len(lines[0])
d['maxy'] = len(lines)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        d[(x,y)] = int(c)
        unvisited.add((x,y))
ic(d)
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
