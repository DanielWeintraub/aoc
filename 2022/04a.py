import sys
from icecream import ic
from collections import defaultdict

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line.split(","))

ic(lines)

def getSet(input):
    start_end = input.split("-")
    pos = [ x for x in range(int(start_end[0]), int(start_end[1]) + 1) ]
    ic(pos)
    return set(pos)


elf_pairs = []
for line in lines:
    ic(line)
    elf1 = getSet(line[0])
    elf2 = getSet(line[1])
    elf_pairs.append((elf1,elf2))


ic(elf_pairs)

overlapping_pairs = 0
for elf_pair in elf_pairs:
    if elf_pair[0].issubset(elf_pair[1]) or elf_pair[1].issubset(elf_pair[0]):
        overlapping_pairs = overlapping_pairs + 1

ic(overlapping_pairs)
