import sys
from icecream import ic

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)

ic(lines)

def getPriority(i):
    p = ord(i)
    if p > 91:
        p = p - 96
    else:
        p = p - 38
    ic(p)
    return p

ps = 0
for line in lines:
    ic(line)
    mi = int(len(line) / 2)
    fc = line[:mi]
    sc = line[mi:]
    ic(fc,sc)
    for i in fc:
        if i in sc:
            ic("Match", i)
            ps = ps + getPriority(i)
            break

ic(ps)
