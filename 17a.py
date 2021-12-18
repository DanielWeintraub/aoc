from collections import defaultdict
import sys
from icecream import ic
import re

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)
nums = re.findall(r'-?\d+', lines[0])
nums = list(map(int,nums))
ic(nums)

def decr(x):
    if x < 0:
        return x -1
    elif x > 0:
        return x -1
    else:
        return 0

def between(n, r1, r2):
    if r1>r2:
        return n >= r2 and n <= r1
    if r2>r1:
        return n >= r1 and n <= r2
    else:
        sys.exit("a")

def inclusive_range(one, two):
    if one <= two:
        return range(one, two+1, 1)
    else:
        return range(one, two-1, -1)

pos = (0,0)
poss = [pos]
y_max = 0
ivs = []
for gyv in inclusive_range(-500,10000):
    for gxv in inclusive_range(0,300):
        #ic(gyv,gxv)
        pos = (0,0)
        poss = [pos]
        xv = gxv
        yv = gyv
        while abs(pos[0]) < 200 and abs(pos[1]) < 50000:
            npos = (pos[0] + xv, pos[1] + yv)
            poss.append(npos)
            pos = npos
            xv = decr(xv)
            yv = yv - 1
        
            if between(pos[0], nums[0], nums[1]) and between(pos[1], nums[2], nums[3]):
                #ic("YES", pos)
                ivs.append((gxv,gyv))
                localymax=0
                for p in poss:
                    if p[1]> localymax:
                        localymax = p[1]
                if localymax > y_max:
                    y_max = localymax
                break
        #ic(poss)
ic(y_max)
ic(ivs)
ic(len(ivs))
