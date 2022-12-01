from collections import defaultdict
import sys
from icecream import ic
import json

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
        self.parent = None

def parse(l):
    base = Node("sn")
    if isinstance(l[0],int):
        base.left = Node(int(l[0]))
    elif isinstance(l[0],list):
        base.left = parse(l[0])
    else:
        sys.exit("a")
    base.left.parent = base
    if isinstance(l[1],int):
        base.right = Node(int(l[1]))
    elif isinstance(l[1],list):
        base.right = parse(l[1])
    else:
        sys.exit("b")
    base.right.parent = base
    return base

def explode(n):
    i1 = n.left
    i2 = n.right
    par = n.parent
    n = Node(0)
    n.parent = par

def reduce(t,d=0):
    if t.left.data == "sn":
        reduce(t.left, d=d+1)
    if t.right.data == "sn":
        reduce(t.right, d=d+1)
    if d > 3:
        print("explode")
        printTree(t)
        explode(t)
    return t

#def reduce(t):
#    currentNode = t
#    stack = []
#    visitedNodes = set()
#    while True:
#        ic(currentNode, len(stack))
#        if currentNode.data == "sn" and not currentNode in visitedNodes:
#            stack.append(currentNode)
#            visitedNodes.add(currentNode)
#            currentNode = currentNode.left
#        elif isinstance(currentNode.data,int):
#            ic(currentNode.data)
#            visitedNodes.add(currentNode)
#            currentNode = stack.pop()
#        elif currentNode.data == "sn" and currentNode in visitedNodes and not currentNode.right in visitedNodes:
#            currentNode = currentNode.right
#        elif currentNode.data == "sn" and currentNode in visitedNodes and currentNode.right in visitedNodes:
#            if not stack:
#                break
#            else:
#                currentNode = stack.pop()

   

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


global tree
def snadd(n1, n2):
    global tree
    base = Node("sn")
    base.left = n1
    n1.parent = base
    base.right = n2
    n2.parent = base
    tree = base
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
