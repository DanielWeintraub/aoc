from collections import defaultdict
import sys
from icecream import ic

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)
ic(lines)

openingC = ['(','[','{','<']
closingC = [')',']','}','>']
scoreT = {')': 3, ']': 57, '}': 1197, '>':25137}

def cMatch(c1,c2):
    if c1 == c2:
        sys.exit("a")
    return abs(ord(c1) - ord(c2)) < 3

def getCloseMatch(c):
    if c == '(':
        return ')'
    elif c == '[':
        return ']'
    elif c == '{':
        return '}'
    elif c == '<':
        return '>'
    else:
        sys.exit("b") 

linesc = lines.copy()
comps = []
for line in linesc:
    ic(line)
    stack=[]
    comp=[]
    err = False
    for c in line:
        if c in openingC:
            stack.append(c)
        else:
            if cMatch(c, stack[-1]):
                stack.pop()
            else:
                ic("syntax error",c)
                lines.remove(line)
                err = True
                break
    if not err:
        stack.reverse()
        for c in stack:
            comp.append(getCloseMatch(c))
        ic(comp)
        comps.append("".join(comp))

ic(lines)
ic(comps)

nscore = { ')': 1, ']': 2, '}': 3, '>':4}

scores = []
for co in comps:
    cscore = 0
    for c in co:
        cscore = cscore * 5
        cscore = cscore + nscore[c]
        ic(cscore)
    scores.append(cscore)

ic(scores)
scores.sort()
middleIndex = (len(scores) - 1)/2
ic(scores[int(middleIndex)])

