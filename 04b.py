from collections import defaultdict
import sys
from icecream import ic

filename = sys.argv[1]
ic(filename)

lines_d = []
with open(filename) as file:
    while (line := file.readline()):
        lines_d.append(line)

lines = []
for line in lines_d:
    lines.append(line.rstrip())

ic(lines)

bns = lines[0].split(',')
ic(bns)

def getBoards( inp ):
    ic("getBoards")
    if len(inp) < 1:
        sys.exit("a")
    if not inp[0]:
        return getBoards(inp[1:])
    if len(inp) == 5:
        #Do the thing
        board = {}
        for y in range(5):
            for x, v in enumerate(inp[y].split()):
                board[(x, y)] = {"num": v, "picked": False }
        ic("returning",board)
        return [ board ]
    else:
        nf = inp[:5]
        rf = inp[6:]
        ans = [ *getBoards(nf), *getBoards(rf) ]
        return ans

def printBoard(board):
    ic("printBoard")
    #ic(type(board))
    for y in range(5):
        line = ""
        for x in range(5):
            line += board[(x,y)]["num"]
            if board[(x,y)]["picked"]:
                line += "*"
            line += "  "
        print(line)

boards = getBoards(lines[1:])
ic(boards, len(boards))

for board in boards:
    printBoard(board)

def markPick( board, n ):
    for y in range(5):
        for x in range(5):
            if board[(x,y)]["num"] == n:
                board[(x,y)]["picked"] = True

def isWinner(board):
    for y in range(5):
        winners = 0
        for x in range(5):
            if board[(x,y)]["picked"]:
                winners += 1
        if winners == 5:
            return True
    for y in range(5):
        winners = 0
        for x in range(5):
            if board[(y,x)]["picked"]:
                winners += 1
        if winners == 5:
            return True

def findBoardSum(board,n):
    sum = 0
    for y in range(5):
        for x in range(5):
            if not board[(x,y)]["picked"]:
                sum += int(board[(x,y)]["num"])
    return ( sum * int(n))



# Start Playing Bingo
for n in bns:
    ic("Playing Bingo!", n)
    for board in boards:
        markPick( board, n )
    for board in boards:
        printBoard(board)
    boardsToRemove = []
    for board in boards:
        if isWinner(board):
            ic("Winning Board",board)
            ic(findBoardSum(board,n))
            boardsToRemove.append(board)
    for board in boardsToRemove:
        boards.remove(board)
