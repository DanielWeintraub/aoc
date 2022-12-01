from collections import defaultdict
import sys
from icecream import ic

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)

fishl = [ int(x) for x in lines[0].split(",") ]
ic(fishl)
d = {}
for i in range(9):
    d[i] = 0
for fish in fishl:
    d[fish] += 1
print("**Starting state")
ic(d)
print("**")
for i in range(1,80+1):
    ic(i)
    d2 = {}
    for j in range(9):
        if j == 0:
            d2[6] = d[0]
            d2[8] = d[0]
        else:
            if (j-1) in d2.keys():
                d2[j-1] += d[j]
            else:
                d2[j-1] = d[j]
        ic(d2)
    d = d2.copy()
    print("**End of day {}".format(i))
    ic(d)
    print("**")

ic(d)

sum = 0
for v in d.values():
    sum += v

ic(sum)
