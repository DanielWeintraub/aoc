import sys
import re
from icecream import ic
from collections import defaultdict

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line.split(": ")[1])

ic(lines)
cards = []
for line in lines:
    cards.append(([int(n) for n in line.split(" | ")[0].split(" ") if n],[int(n) for n in line.split(" | ")[1].split(" ") if n]))

ic(cards)

cn = [1 for _ in range(len(cards))]
for i, card in enumerate(cards):
    start_cn = cn[i]
    ic(i, start_cn)
    wins = 0
    for n in card[1]:
        if n in card[0]:
            wins += 1
    ic(wins)
    for j in range(wins):
        cn[i+j+1] += 1 * start_cn

ic(cn)
ic(sum(cn))
