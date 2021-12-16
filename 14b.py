from collections import defaultdict
from collections import namedtuple
import sys
from icecream import ic

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)
inp = lines[0]
ic(inp)
d = {}
with open(filename) as file:
    while (line := file.readline()):
        if '->' in line:
            lp = line.rstrip().split(' -> ')
            d[lp[0]] = lp[1]
ic(d)
mydd = defaultdict(int)
for i in range(len(inp)-1):
    mydd[inp[i] + inp[i+1]] += 1
for j in range(40):
    ic(mydd)
    outp = defaultdict(int)
    ic(outp)
    for k, v in mydd.items():
        ic(k,v)
        outp[k[0] + d[k]] += v
        outp[d[k] + k[1]] += v
    ic(outp)
    count = defaultdict(int)
    for k, v in outp.items():
        count[k[0]] += (v/2)
        count[k[1]] += (v/2)
    count[inp[0]] += .5
    count[inp[-1]] += .5
    ic(j+1,count)
    mydd = outp.copy()
