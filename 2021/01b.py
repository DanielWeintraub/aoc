import sys
from icecream import ic

filename = sys.argv[1]
ic(filename)
data = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        data.append(line)

data2 = [ int(x) for x in data ]
ic(data2)

numIncreasing = 0
for i in range(1,len(data2)-2):
    ic(i)
    ic( data2[i-1:i+2] )
    ic( data2[i:i+3] )
    if sum(data2[i:i+3]) > sum(data2[i-1:i+2]):
        numIncreasing += 1

ic(numIncreasing)
