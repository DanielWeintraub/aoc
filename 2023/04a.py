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

scores = []
for card in cards:
    card_score = 0
    for n in card[1]:
        if n in card[0]:
            if card_score == 0:
                card_score = 1
            else:
                card_score *= 2
    scores.append(card_score)

ic(sum(scores))
