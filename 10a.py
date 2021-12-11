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

score=0
for line in lines:
    ic(line)
    stack=[]
    for c in line:
        if c in openingC:
            stack.append(c)
        else:
            if cMatch(c, stack[-1]):
                stack.pop()
            else:
                ic("syntax error",c)
                score += scoreT[c]
                break
        #ic(stack)

ic(score)


#for line in lines:
#    oc = 0
#    for c in openingC:
#        oc += line.count(c)
#    cc = 0
#    for c in closingC:
#        cc += line.count(c)
#    ic(oc)
#    ic(cc)
