import sys
import re
from icecream import ic
from collections import defaultdict

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)

just_numbers = [re.sub(r'[a-z]', '', line) for line in lines]
#ic(just_numbers)
sums = [(line[0] + line[-1]) for line in just_numbers]
#ic(sums)
# Now add all the sums together
total = 0
for sum in sums:
    total += int(sum)
ic(total)
