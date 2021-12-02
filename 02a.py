from collections import defaultdict
import sys
from icecream import ic

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)

d = defaultdict(int)
for line in lines:
    bits = line.split()
    d[bits[0]] += int(bits[1])

ic(d)

ic(d['forward'])

ic(d['forward'] * ( d['down'] - d['up'] ))


