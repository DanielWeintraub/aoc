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

highestCal = 0
for elf in elves:
    total = sum(elf)
    if total > highestCal:
        highestCal = total

ic(highestCal)

