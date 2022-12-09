import sys
from icecream import ic
from collections import defaultdict
import re
import itertools

ic.disable()

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline()):
        lines.append(line.rstrip())

ic(lines)

window = 14

for line in lines:
    ic(line)
    for c in range(window,len(line)+1):
        ic(line[c-window:c])
        se = len(set([*line[c-window:c]]))
        ic(se)
        if se == window:
            print(c)
            break

