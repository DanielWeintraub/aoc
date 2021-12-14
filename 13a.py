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
folds = []
with open(filename) as file:
    while (line := file.readline()):
        if "fold" in line:
            folds.append(line.rstrip())
ic(folds)
d = defaultdict(int)
for line in lines:
    d[(int(line.split(",")[0]),int(line.split(",")[1]))] += 1
ic(d)
maxP = namedtuple('maxP', ['x', 'y'])

def getMaxX(d):
    maxX = 0
    for key in d.keys():
        if key[0] > maxX:
            maxX = key[0]
    return maxX

def getMaxY(d):
    maxY = 0
    for key in d.keys():
        if key[1] > maxY:
            maxY = key[1]
    return maxY

def drawGrid(d, num=False):
    for y in range(getMaxY(d) + 1):
        newline = ""
        for x in range(getMaxX(d) + 1):
            if d[(x,y)] > 0:
                if num:
                    newline += str(d[(x,y)])
                else:
                    newline += "#"
            else:
                newline += "."
        print(newline)
    print()

def countDots(d):
    count = 0
    for y in range(getMaxY(d) + 1):
        for x in range(getMaxX(d) + 1):
            if d[(x,y)] > 0:
                count += 1
    return count

def foldGrid(d, direction, n):
    ic(direction, n)
    if direction == 'y':
        for y in range(n+1, getMaxY(d) + 1):
            for x in range(0, getMaxX(d) + 1):
                d[(x, n - (y-n))] += d[(x,y)]
        dkeys = list(d.keys())
        for p in dkeys:
            if p[1] >= n:
                del d[p]
    elif direction == 'x':
        for x in range(n+1, getMaxX(d) + 1):
            for y in range(0, getMaxY(d) + 1):
                d[(n - (x-n), y)] += d[(x,y)]
        dkeys = list(d.keys())
        for p in dkeys:
            if p[0] >= n:
                del d[p]
    return d


#drawGrid(d)

for fold in folds:
    n = int(fold.split("=")[-1])
    direction = fold.split('=')[0][-1]
    d2 = foldGrid(d, direction, n)
    #drawGrid(d2, num=True)
    ic(countDots(d2))
    break
