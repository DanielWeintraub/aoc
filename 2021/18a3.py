#I cribbed basically all of this from here:
#https://github.com/benediktwerner/AdventOfCode/blob/master/2021/day18/sol.py

from collections import defaultdict
import sys
from icecream import ic
import json
import math

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(json.loads(line))
ic(lines)

def addl( sn, n ):
    if n is None:
        #sys.exit("a")
        return sn
    if isinstance(sn, int):
        return sn+n
    return [ addl(sn[0], n), sn[1] ]

def addr( sn, n ):
    if n is None:
        return sn
    if isinstance(sn, int):
        return sn+n
    return [sn[0], addr(sn[1], n)]

def explode( sn, d = 0 ):
    ic("ex", sn, d)
    if isinstance(sn,int):
        return False, None, sn, None
    if d == 4:
        return True, sn[0], 0, sn[1]
    l = sn[0]
    r = sn[1]
    ex, le, l, re = explode( l, d+1 )
    ic("1",ex)
    if ex:
        return True, le, [l, addl(r, re)], None
    ex, le, r, re = explode( r, d+1 )
    ic("2",ex)
    if ex:
        return True, None, [addr(l, le), r], re
    return False, None, sn, None

def split(sn):
    if isinstance(sn, int):
        if sn >= 10:
            return True, [sn // 2, math.ceil(sn / 2)]
        return False, sn
    a, b = sn
    change, a = split(a)
    if change:
        return True, [a, b]
    change, b = split(b)
    return change, [a, b]

def getMag(sn):
    if isinstance(sn, int):
        return sn
    else:
        return (3 * getMag(sn[0])) + (2 * getMag(sn[1]))

def snadd( sn1, sn2 ):
    snsum = [sn1,sn2]
    while True:
        ic("t")
        changed, _, snsum, _ = explode( snsum )
        if changed:
            continue
        changed, snsum = split(snsum)
        if not changed:
            break
    return snsum

snsum = lines[0]
#for i in range(1,2):
for i in range(1,len(lines)):
    snsum = snadd( snsum, lines[i])
ic('yes')
ic(snsum)

ic(getMag(snsum))
