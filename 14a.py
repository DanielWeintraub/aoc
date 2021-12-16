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
outp = ''
for j in range(40):
    if outp:
        inp = outp
        outp = ""
    for i in range(len(inp) - 1):
        #ic(i)
        #ic(inp[i] + inp[i+1])
        outp += inp[i]
        if inp[i] + inp[i+1] in d.keys():
            outp += d[inp[i] + inp[i+1]]
        #ic(outp)
    outp += inp[-1]
  #  ic(j+1,outp)

ic("****")
ic(outp)

os = set(outp)
cd = {}
for c in os:
    cd[c] = outp.count(c)
ic(cd)
