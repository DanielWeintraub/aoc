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

ic(lines)
# step through each line
# find each number that's spelled out
# replace it with the number
r = []
for line in lines:
    ic(line)
    remainder = line
    result = ''
    while remainder:
        remainder = re.sub(r'^one', '1', remainder)
        remainder = re.sub(r'^two', '2', remainder)
        remainder = re.sub(r'^three', '3', remainder)
        remainder = re.sub(r'^four', '4', remainder)
        remainder = re.sub(r'^five', '5', remainder)
        remainder = re.sub(r'^six', '6', remainder)
        remainder = re.sub(r'^seven', '7', remainder)
        remainder = re.sub(r'^eight', '8', remainder)
        remainder = re.sub(r'^nine', '9', remainder)
        #remainder = re.sub(r'^zero', '0', remainder)
        # remove the first character from remainder
        result += remainder[0]
        remainder = remainder[1:]
    ic(result)
    r.append(result)
ic(r)

r2 = []
for line in lines:
    # reverse the line
    line = line[::-1]
    ic(line)
    remainder = line
    result = ''
    while remainder:
        remainder = re.sub(r'^eno', '1', remainder)
        remainder = re.sub(r'^owt', '2', remainder)
        remainder = re.sub(r'^eerht', '3', remainder)
        remainder = re.sub(r'^ruof', '4', remainder)
        remainder = re.sub(r'^evif', '5', remainder)
        remainder = re.sub(r'^xis', '6', remainder)
        remainder = re.sub(r'^neves', '7', remainder)
        remainder = re.sub(r'^thgie', '8', remainder)
        remainder = re.sub(r'^enin', '9', remainder)
        #remainder = re.sub(r'^zero', '0', remainder)
        result += remainder[0]
        remainder = remainder[1:]
    r2.append(result[::-1])
ic(r2)



just_numbers = [re.sub(r'[a-z]', '', line) for line in r]
just_numbers2 = [re.sub(r'[a-z]', '', line) for line in r2]
ic(just_numbers)
ic(just_numbers2)
sums = [(line[0] + line2[-1]) for line,line2 in zip(just_numbers, just_numbers2)]
ic(sums)
# Now add all the sums together
total = 0
for sum in sums:
    total += int(sum)
ic(total)
