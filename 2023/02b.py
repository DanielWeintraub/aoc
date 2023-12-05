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

def get_fewest(game):
    # Find the fewest number of cubes that can be present to make the game possible
    max_r, max_g, max_b = 0,0,0
    for rounda in game:
        ic(rounda)
        if rounda[0] > max_r:
            max_r = rounda[0]
        if rounda[1] > max_g:
            max_g = rounda[1]
        if rounda[2] > max_b:
            max_b = rounda[2]
    return (max_r, max_g, max_b)

sum = 0
for game in data:
    ic(game)
    max_r, max_g, max_b = get_fewest(game)
    ic(max_r, max_g, max_b)
    sum += max_r * max_g * max_b

ic(sum)
