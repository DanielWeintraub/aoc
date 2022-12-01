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
    l = inp.copy()
    m = {}
    m2 = {}
    for e in inp:
        ic(e)
        if len(e) == 2:
            m[2] = "".join(sorted(e))
            m2["".join(sorted(e))] = 2
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
    
    ic(l)
    asdf=[]
    for li in l:
        asdf.append("".join(sorted(li)))
    print(sorted(asdf))
    return m2

ic(findMap(data[0]["all"]))

def countDDigits(d):
    m = findMap(d["all"])
    count = 0
    for sn in d["l4"]:
        if "".join(sorted(sn)) in m:
            count += 1
    return count

    
bigCount = 0
for datum in data:
    bigCount += countDDigits(datum)
ic(bigCount)
