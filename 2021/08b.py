#Wow I'm really not pleased with this one.

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
data = []
for line in lines:
    d = {}
    l = line.split(" | ")
    d["all"] = " ".join(l).split()
    d["l4"] = l[1].split()
    ic(d)
    data.append(d)

ic(data)

def findMap(inp):
    ic("lets make a map")
    l = inp.copy()
    m = {}
    m2 = {}
    for e in inp:
        if len(e) == 2:
            m[1] = "".join(sorted(e))
            m2["".join(sorted(e))] = 1
            l.remove(e)
        elif len(e) == 3:
            m[7] = "".join(sorted(e))
            m2["".join(sorted(e))] = 7
            l.remove(e)
        elif len(e) == 4:
            m[4] = "".join(sorted(e))
            m2["".join(sorted(e))] = 4
            l.remove(e)
        elif len(e) == 7:
            m[8] = "".join(sorted(e))
            m2["".join(sorted(e))] = 8
            l.remove(e)
    ic(m)
    ic(l)
    ic("Now try to find 5")
    fourString = m[4]
    oneString = m[1]
    subString = "".join( c for c in fourString if c not in oneString )
    ic(subString)
    listCopy = l.copy()
    for e in listCopy:
        ic("".join(sorted(e)))
        if subString[0] in "".join(sorted(e)) and subString[1] in "".join(sorted(e)) and len(e) == 5:
            ic("Found 5")
            m[5] = "".join(sorted(e))
            m2["".join(sorted(e))] = 5
            l.remove(e)
    ic(m)
    ic(l)
    ic("Let's find 3")
    sevenString = m[7]
    chars = set(sevenString)
    listCopy = l.copy()
    for e in listCopy:
        ic("".join(sorted(e)))
        if len(e) == 5 and sevenString[0] in e and sevenString[1] in e and sevenString[2] in e:
            ic("Found 3")
            m[3] = "".join(sorted(e))
            m2["".join(sorted(e))] = 3
            l.remove(e)
    ic(m)
    ic(l)
    ic("Let's find 2?")
    listCopy = l.copy()
    for e in listCopy:
        ic("".join(sorted(e)))
        if len(e) == 5:
            ic("Maybe found 2?")
            m[2] = "".join(sorted(e))
            m2["".join(sorted(e))] = 2
            l.remove(e)
    ic(m)
    ic(l)
    ic("Let's find 9")
    if 4 in m.keys() and 3 in m.keys():
        ic("Found 9")
        m[9] = "".join(sorted(list(set(m[4]) | set(m[3]))))
        ic(m[9])
        m2[m[9]] = 9
        listCopy = l.copy()
        for e in listCopy:
            if m[9] == "".join(sorted(e)):
                l.remove(e)
    ic(m)
    ic(l)
    ic("Let's find 6")
    fiveString = m[5]
    chars = set(fiveString)
    listCopy = l.copy()
    for e in listCopy:
        ic("".join(sorted(e)))
        if len(e) == 6 and fiveString[0] in e and fiveString[1] in e and fiveString[2] in e and fiveString[3] in e and fiveString[4] in e:
            ic("Found 6")
            m[6] = "".join(sorted(e))
            m2["".join(sorted(e))] = 6
            l.remove(e)
    ic(m)
    ic(l)
    # Let's find 0
    listCopy = l.copy()
    for e in listCopy:
        ic("".join(sorted(e)))
        if len(e) == 6:
            ic("Found 0 maybe")
            m[0] = "".join(sorted(e))
            m2["".join(sorted(e))] = 0
            l.remove(e)
    ic(m)
    ic(l)
    ic("Unidentified Segment Codes")
    ic(l)
    return m2

def getLast4( inp ):
    m = findMap(inp["all"])
    snum = ""
    for code in inp["l4"]:
        snum += str(m["".join(sorted(code))])
    return snum


print("*********")
    
answers = []
for datum in data:
    answers.append(getLast4(datum))
ic(sum([int(x) for x in answers]))
#ic(getLast4(data[1]))
