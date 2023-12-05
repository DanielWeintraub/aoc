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
mymap = {}
max_y = len(lines)
max_x = len(lines[0])

ic(max_x, max_y)

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        mymap[(x, y)] = c

ic(mymap[(0, 0)])
ic(mymap[(max_x-1, max_y-1)])

def isdigit(s):
    # return true is s is a digit
    return re.match(r'\d', s)

# Walk through the map and create a map of the numbers
numbers = []
for y in range(max_y):
    x=0
    while x < max_x:
        # If the element at this point is a number, start following it
        if mymap[(x, y)].isdigit():
            ic("Found a number at", x, y)
            found_x = x
            number = mymap[(x, y)]
            # Follow the number until we hit the end
            # we can only go right
            x += 1
            if x < max_x:
                ic(x,max_x)
                while mymap[(x, y)].isdigit():
                    ic((x,y))
                    number += mymap[(x, y)]
                    if x + 1 < max_x:
                        x += 1
                    else:
                        break
                ic(number)
            else:
                ic("We are at the end of the line")
            numbers.append(((found_x,y),int(number)))
        x += 1

def has_neighboring_symbol(mymap, x, y):
    # Check if the element at this point has a neighboring symbol
    for mx in range(x-1, x+2):
        for my in range(y-1, y+2):
            ic(mx, my)
            if (mx,my) in mymap.keys():
                if not mymap[(mx,my)].isdigit() and not mymap[(mx,my)] == '.':
                    return True
    return False

ans = 0
# Find if any numbers have a neighoring symbol
for loc, num in numbers:
    ic(loc, num)
    for nx in range(len(str(num))):
        if has_neighboring_symbol(mymap, loc[0]+nx, loc[1]):
            ic("Found a neighboring symbol for", loc, num)
            ans += num
            break

ic(ans)

