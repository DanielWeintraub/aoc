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
aim = 0
for line in lines:
    bits = line.split()
    bits[1] = int(bits[1])
    if bits[0][0] == 'd':
        aim += bits[1]
    elif bits[0][0] == 'u':
        aim -= bits[1]
    elif bits[0][0] == 'f':
        d["x"] += bits[1]
        d["y"] += (aim * bits[1])
    else:
        sys.exit("blerg")

ic( d["x"] * d["y"] )
