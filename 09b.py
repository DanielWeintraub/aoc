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
d['maxx'] = len(lines[0])
d['maxy'] = len(lines)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        d[(x,y)] = int(c)
ic(d)

def isLowPoint( d, x, y ):
    ic(x,y,d[(x,y)])
    lp = True
    for p in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
        if p in d.keys():
            lp = d[(x,y)] < d[p]
            #ic(p)
            #ic(lp)
            if not lp:
                return False
    ic("Found Low Point")
    ic(d[(x,y)])
    return lp

#ic(isLowPoint(d, 1, 0))

def findCandidates(d, x, y):
    #ic("find",(x,y))
    candidates = []
    for p in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
        #ic('Testing',p)
        if p in d.keys() and d[p] != 9:
            #ic("Append",p)
            candidates.append(p)
    #ic(candidates)
    return candidates

def findBasin(d, x, y):
    basin = set()
    basin.add((x,y))
    while True:
        nb = basin.copy()
        #ic("Find loop",nb)
        for p in basin:
            #ic(p)
            nc = findCandidates(d, p[0], p[1])
            ncs = set(nc)
            #ic(ncs)
            nb = set.union(nb, ncs)
            #ic(nb)
        if basin == nb:
            return basin
        basin = nb.copy()

lowPoints = []
for y in range(d['maxy']):
    for x in range(d['maxx']):
        if isLowPoint(d, x, y):
            lowPoints.append((x,y))

ic(lowPoints)
sizes = []
for lp in lowPoints:
    b = findBasin(d,lp[0],lp[1])
    sizes.append(len(b))
#ic(findBasin(d,1,0)) 
sizes.sort()
ic(sizes)

ic(sizes[-1] * sizes[-2] * sizes[-3])


