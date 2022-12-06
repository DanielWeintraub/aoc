import sys
from icecream import ic
from collections import defaultdict

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)

ic(lines)

groups = defaultdict(list)
for i in range(len(lines)):
    groups[int(i/3)].append(lines[i])

ic(groups)

def getPriority(i):
    p = ord(i)
    if p > 91:
        p = p - 96
    else:
        p = p - 38
    ic(p)
    return p

ps = 0
for group in groups.values():
    ic(group)
    items = set()
    for inv in group:
        for item in inv:
            items.add(item)
    #ic(items)
    ic("groupdone")

    for item in items:
        ic(item)
        inv_w_items = 0
        for inv in group:
            ic(inv)
            if item in inv:
                inv_w_items = inv_w_items + 1
                ic(inv_w_items)
            if inv_w_items == 3:
                ic("Match", item)
                ps = ps + getPriority(item)
                break

ic(ps)
