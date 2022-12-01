from collections import defaultdict
from collections import namedtuple
import sys
from icecream import ic

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)
ic(lines)
d = {}
maxP = namedtuple('maxP', ['x', 'y'])
d['max'] = maxP(x=len(lines[0]), y=len(lines))
ic(d['max'])
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        d[(x,y)] = int(c)
#ic(d)

def printBoard( d ):
    for y in range(d['max'].y):
        myl = ""
        for x in range(int(d['max'].x)):
            if d[(x,y)] <= 9:
                myl += str(d[(x,y)])
            else:
                myl += "*"
        print(myl)
    print("")

def findOver( d ):
    nineList = []
    for k, v in d.items():
        if isinstance(v, int):
            if v > 9:
                nineList.append(k)
    #ic(nineList)
    return nineList

def flashNine( d, nine ):
    #if not d[nine] == 9:
        #sys.exit("It's not a nine :|")
    for y in range(nine[1]-1, nine[1]+2):
        for x in range(nine[0]-1, nine[0]+2):
            if (x, y) in d.keys():
                d[(x,y)] += 1

def flashNines( d, nines ):
    for nine in nines:
        #ic(nine)
        flashNine( d, nine )

def resetFlashed( d, points ):
    for p in points:
        d[p] = 0

print("Initial Board:")
printBoard(d)
flashes=0

for step in range(1, 101):
    ic(step)
    # Increase every octopus
    for point in d.keys():
        if isinstance(d[point], int):
            d[point] += 1
    printBoard(d)
    flashList = set()
    newList = findOver(d)
    while newList:
        over = findOver(d)
        newList = [x for x in over if not x in flashList]
        #ic(over, newList)
        flashNines(d, newList)
        flashList.update(newList)
        #ic(flashList)
    resetFlashed(d,flashList)
    flashes += len(flashList)
    print("End of Step {}".format(step))
    printBoard(d)

ic(flashes)
