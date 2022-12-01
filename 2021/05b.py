from collections import defaultdict
import sys
from icecream import ic

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)

board = defaultdict(int)
ic(lines)

ls=[]
for line in lines:
    t = line.split(" -> ")
    t1 = t[0].split(",")
    t2 = t[1].split(",")
    ls.append([(int(t1[0]),int(t1[1])),(int(t2[0]),int(t2[1]))])

ic(ls)

#Find Boards Maxes:
for l in ls:
    for p in l:
        if board['xmax'] < p[0]:
            board['xmax'] = p[0]
        if board['ymax'] < p[1]:
            board['ymax'] = p[1]

ic(board['xmax'], board['ymax'])

def printBoard(board):
    print("***")
    for y in range(board['ymax']+1):
        pline = ""
        for x in range(board['xmax']+1):
            if board[(x,y)] == 0:
                pline += "."
            else:
                pline += str(board[(x,y)])
        print(pline)

#board[(1,1)] = 3
#board[(9,9)] = 4
#printBoard(board)
#sys.exit()

def inclusive_range(one, two):
    if one <= two:
        return range(one, two+1, 1)
    else:
        return range(one, two-1, -1)

#draw lines on board
for l in ls:
    ic(l)
    if l[0][0] == l[1][0] or l[0][1] == l[1][1]:
        ic("not diagonal")
        if l[0][0] == l[1][0]:
            #Vert
            print("Vert")
            for i in range(min([l[0][1],l[1][1]]),max([l[0][1],l[1][1]])+1):
                ic(i)
                board[(l[0][0],i)] += 1
        else:
            #hor
            print("Hori")
            for i in range(min([l[0][0],l[1][0]]),max([l[0][0],l[1][0]])+1):
                ic(i)
                board[(i,l[0][1])] += 1
        #printBoard(board)
    else:
        ic("diagonal")
        for y, x in zip(inclusive_range(l[0][1],l[1][1]),inclusive_range(l[0][0],l[1][0])):
            ic(x,y)
            board[(x,y)] +=1


#print board
printBoard(board)

ans = 0
for y in range(board['ymax']+1):
    for x in range(board['xmax']+1):
        if board[(x,y)] > 1:
            ans += 1
ic(ans)
