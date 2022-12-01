from collections import defaultdict
import sys
from icecream import ic
import numpy

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)
ic(lines)
inp = lines[0]

hbmap = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
        }

def hextob( hexin ):
    bout = ""
    for c in hexin:
        bout += hbmap[c]
    return bout

def decode(inp):
    ic("decoding",inp)
    if not inp:
        return None, None
    np = {}
    np['version'] = int(inp[:3],2)
    inp = inp[3:]
    ic(np,inp)
    np['typeID'] = int(inp[:3],2)
    inp = inp[3:]
    ic(np,inp)
    if np['typeID'] == 4:
        ic("boring packet")
        np['data'] = []
        keepGoing = True
        while keepGoing:
            keepGoing = bool(int(inp[:1]))
            inp = inp[1:]
            np['data'].append(inp[:4])
            inp = inp[4:]
            ic("left overA", inp)
            ic("a",np,inp,keepGoing)
        return np, inp
    else:
        np['operatorMode'] = inp[:1]
        inp = inp[1:]
        ic(np['operatorMode'],inp)
        np['data'] = []
        if np['operatorMode'] == "0":
            length = int(inp[:15],2)
            ic(length)
            inp = inp[15:]
            ic(inp)
            subps = inp[:length]
            ic(subps)
            while subps:
                result, remainder = decode(subps)
                np['data'].append(result)
                subps = remainder
            remainder2 = inp[length:]
            return np, remainder2
        if np['operatorMode'] == "1":
            n = int(inp[:11],2)
            ic(n)
            inp = inp[11:]
            for i in range(n):
                result, remainder = decode(inp)
                np['data'].append(result)
                inp = remainder
            return np, remainder
    sys.exit("uh oh")

operations = [
        sum,
        numpy.prod,
        min,
        max,
        sys.exit,
        lambda i:int(i[0] > i[1]),
        lambda i:int(i[0] < i[1]),
        lambda i:int(i[0] == i[1])
        ]

def getV( data ):
    ic(data)
    v = 0
    if data is None:
        sys.exit("what")
    elif isinstance(data,str):
        sys.exit('huh')
    if data['typeID'] == 4:
        ic(int("".join(data['data']),2))
        return int("".join(data['data']),2)
    else:
        ic(data['typeID'])
        v = 0
        sps = []
        for sp in data['data']:
           sps.append(getV(sp))
        ic(sps)
        v = operations[data['typeID']](sps)
        return v
    sys.exit("whoops")

binp = hextob(inp)
outp = []
while binp:
    ic("main while")
    result, remainder = decode(binp)
    outp.append(result)
    binp = remainder
    ic(binp)
    if binp:
        if int(binp, 2) == 0:
            binp = ""
ic(outp)
ic("***********************")
ic(getV(outp[0]))
