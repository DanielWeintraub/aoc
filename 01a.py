

import sys
from icecream import ic

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)

numIncreasing = 0
for i in range(1,len(lines)):
    ic(lines[i])
    if int(lines[i]) > int(lines[i-1]):
        ic(lines[i], lines[i-1])
        numIncreasing += 1

ic(numIncreasing)
