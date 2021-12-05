from collections import defaultdict
import sys
from icecream import ic

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)

def getFreq(inp):
    ic("getFreq")
    dd = defaultdict(int)
    for d in range(len(inp[0])):
        ic(d)
        for line in inp:
            l = []
            l.append(line[d])
            for n in ['0','1']:
                dd[(d,n)] += l.count(n)
    return dd

dd = getFreq(lines)
ic(dd)

def getO(inp,pos=0):
    ic("getO")
    dd = getFreq(inp)
    ic(dd, inp)
    if len(inp) == 1:
        return inp
    nl = []
    if dd[(pos,'0')] > dd[(pos,'1')]:
        for le in inp:
            if le[pos] == '0':
                ic(le)
                nl.append(le)
    else:
        for le in inp:
            if le[pos] == '1':
                ic(le)
                nl.append(le)
    return getO(nl, pos=pos+1)


def getC(inp,pos=0):
    ic("getO")
    dd = getFreq(inp)
    ic(dd, inp)
    if len(inp) == 1:
        return inp
    nl = []
    if dd[(pos,'1')] >= dd[(pos,'0')]:
        for le in inp:
            if le[pos] == '0':
                ic(le)
                nl.append(le)
    else:
        for le in inp:
            if le[pos] == '1':
                ic(le)
                nl.append(le)
    return getC(nl, pos=pos+1)

oxg = getO(lines)[0]

cos = getC(lines)[0]
ic(oxg)
ic(cos)


ans = int(oxg, 2) * int(cos, 2)
ic(ans)
