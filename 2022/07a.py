import sys
from icecream import ic
from collections import defaultdict
#import re
#import itertools

#ic.disable()

@dataclass
class finode:
    name: str
    cont: 'typing.Any'

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline()):
        lines.append(line.rstrip())

ic(lines)

wd = ""
for line in lines:
    if "$" in line:
        if "$ cd " in line:
            wd = line.split("$ cd ")[-1]
            ic("new wd",wd)
        if "$ ls " in line:
            ic("ls")
