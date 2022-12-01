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

sum = 0

for y in range(d['maxy']):
    for x in range(d['maxx']):
        if isLowPoint(d, x, y):
            sum += d[(x,y)] + 1

ic(sum)
