from collections import defaultdict
import sys
from icecream import ic
import json
import re

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(json.loads(line))
ic(lines)

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def parse(l):
    base = Node("sn")
    if isinstance(l[0],int):
        base.left = Node(int(l[0]))
    elif isinstance(l[0],list):
        base.left = parse(l[0])
    else:
        sys.exit("a")
    if isinstance(l[1],int):
        base.right = Node(int(l[1]))
    elif isinstance(l[1],list):
        base.right = parse(l[1])
    else:
        sys.exit("b")
    return base

def reduce(t,d=0):
    ts = pt2(t)
    result = ts
    for i,c in enumerate(ts):
        ic(c,d)
        if c == "[":
            d += 1
            if d > 4:
                ic("explode")
                ic(ts[i:])
                match = re.match(r"([0-9]*)",ts[i:])
                exl = match.group(1)
                ic(exl)
                match = re.match(r",\ *(\d*)",ts[i:])
                exr = match.group(1)
                ic(exr)
        elif c == "]":
            d -= 1




    

def printTree(t, d=1):
    iden = "  " * d
    if isinstance(t.data,str):
        print(f"{iden}{t.data}")
        printTree(t.left,d=d+1)
        printTree(t.right,d=d+1)
    elif isinstance(t.data,int):
        print(f"{iden}{t.data}")

def pt2(t, d=1):
    ts = ""
    if isinstance(t.data,str):
        ts += "["
        ts += pt2(t.left, d=d+1)
        ts += ","
        ts += pt2(t.right, d=d+1)
        ts += "]"
    elif isinstance(t.data,int):
        ts += str(t.data)
    return ts


trees = []
for line in lines:
    trees.append( parse(line) )

for tree in trees:
    printTree(tree)
    print()

def snadd(n1, n2):
    base = Node("sn")
    base.left = n1
    base.right = n2
    reduced = reduce(base)
    while pt2(reduced) != pt2(base):
        base = reduced
        ic(base, reduced)
        reduced = reduce(base)
    return reduce(base)

snsum = parse(lines[0])
for i in range(1,2):
    snsum = snadd(snsum, parse(lines[i]))
printTree(snsum)
print(pt2(snsum))
