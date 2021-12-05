from collections import defaultdict
import sys
from icecream import ic

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)

dd = defaultdict(int)
for d in range(len(lines[0])):
    ic(d)
    for line in lines:
        l = []
        l.append(line[d])
        for n in ['0','1']:
            dd[(d,n)] += l.count(n)

ic(dd)

gamma = ""
for i in range(len(lines[1])):
    if dd[(i,'0')] > dd[(i,'1')]:
        gamma += "0"
    else:
        gamma += '1'

ic(gamma)

ep = ''
for c in gamma:
    if c == '0':
        ep += '1'
    else:
        ep += '0'

ic(ep)

ans = int(gamma, 2) * int(ep, 2)
ic(ans)
