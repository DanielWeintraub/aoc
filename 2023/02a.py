import sys
import re
from icecream import ic
from collections import defaultdict

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append((line.split(': ')[0],[x.split(", ") for x in line.split(": ")[1].split("; ")]))



ic(lines)
data=[]

for line in lines:
    game = []
    for rounda in line[1]:
        ic(rounda)
        r,g,b = 0,0,0
        for color in rounda:
            ic(color)
            if "red" in color:
                r = int(color.split(" ")[0])
            if "green" in color:
                g = int(color.split(" ")[0])
            if "blue" in color:
                b = int(color.split(" ")[0])
        ic(r,g,b)
        game.append((r,g,b))
    data.append(game)
ic(data)

total_cubes = (12, 13, 14)

def is_possible(game, total_cubes):
    for rounda in game:
        ic(rounda)
        for colorc, colort in zip(rounda, total_cubes):
            # if the number is greater than the number of cubes, then it is not possible
            if colorc > colort:
                ic("Not possible")
                return False
    ic("Possible")
    return True

answer = 0
for game, gameNumber in zip(data, range(len(data))):
    if is_possible(game, total_cubes):
        answer += gameNumber +1
ic(answer)

