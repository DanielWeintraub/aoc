import sys
from icecream import ic

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(tuple(line.split()))

ic(lines)

def getScore(round):
    ic(round)
    score = 0
    if round[1] == "X":
        score = score + 1
    elif round[1] == "Y":
        score = score + 2
    elif round[1] == "Z":
        score = score + 3
    else:
        sys.exit("error")
    outcome = (ord(round[0]) - (ord(round[1])-23))%3
    ic(outcome)
    if outcome == 0:
        score = score + 3
    elif outcome == 2:
        score = score + 6
    ic(score)
    return score

total = 0
for line in lines:
    total = total + getScore(line)
ic(total)
