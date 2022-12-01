import sys
from icecream import ic

filename = sys.argv[1]
ic(filename)

elves = []
lines = []
with open(filename) as file:
    while (line := file.readline()):
        lines.append(line)

inventory = []
for line in lines:
    ic(line)
    if line.rstrip():
        inventory.append(int(line.rstrip()))
    else:
        elves.append(inventory)
        inventory = []
elves.append(inventory)

ic(elves)

cal = [sum(x) for x in elves]

scal = sorted(cal, reverse=True)
ic(scal)
total = 0
for i in range(3):
    total = total + scal[i]

ic(total)
