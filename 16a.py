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
bhmap = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
        }

versionSum = 0 

def hextob( hexin ):
    bout = ""
    for c in hexin:
        bout += hbmap[c]
    return bout

def decode(inp):
    global versionSum
    ic("decoding",inp)
    if not inp:
        return None, None
    np = {}
    np['version'] = int(inp[:3],2)
    versionSum += np['version']
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
            subp = inp[:length]
            ic(subp)
            remainder = inp[length:]
            result, remainder = decode(inp)
            np['data'].append(result)
            return np, remainder
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


def addV( data ):
    ic(data)
    v = 0
    if data is None:
        return v
    for d in data:
        ic(d)
        if d is None:
            pass
        elif isinstance(d,str):
            pass
        else:
            v += int(d["version"],2)
            ic(v)
            v += addV(d['data'])
    return v

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
#ic(addV(outp))
ic(versionSum)
