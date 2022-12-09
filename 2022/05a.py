import sys
from icecream import ic
from collections import defaultdict
import re
import itertools

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline()):
        lines.append(line)

#ic(lines)

start = []
moves = []
still_start = True
for line in lines:
    if still_start:
        if line.rstrip():
            start.append(line.rstrip())
        else:
            still_start = False
    else:
        moves.append(line.rstrip())

ic(start)
ic(moves)

# Let's prepare the starting board
last_index = int(start[-1].split()[-1])
ic(last_index)
row = len(start)
board = []
for i in range(last_index):
    board.append([])
ic(board)
for i in range(len(start) - 2, -1 ,-1):
    ic(i,start[i])
    c = -1
    for x in range(0,len(start[i]), 4):
        c = c + 1
        ic(c,x)
        elem = start[i][x+1:x+2]
        ic(elem)
        if elem != " ":
            board[c].append(elem)

ic(board)

for move in moves:
    ic(move)
    m = list(itertools.chain(*[l.split(" to ") for l in re.sub("move ", "", move).split(" from ") ]))
    m = [int(i) for i in m]
    ic(m)
    for i in range(m[0]):
        board[m[2]-1].append(board[m[1]-1].pop())
        ic(board)
    
ans = ""
for pile in board:
    ans = ans + pile[-1]
ic(ans)


