from collections import defaultdict
import sys
from icecream import ic

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)

cm = [ int(x) for x in lines[0].split(",") ]
ic(cm)
d = defaultdict(int)
for c in cm:
    d[c] += 1
ic(d)

maxp = max(d.keys())
ic(maxp)

def eToMoveTo(d, pos):
    e = 0
    for k,v in d.items():
        e += (abs(pos - k) * v)
    return e

minE = eToMoveTo(d, 0) 
ic(minE)
for i in range(1,maxp+1):
    ec = eToMoveTo(d, i)
    if ec<minE:
        minE=ec

ic(minE)
