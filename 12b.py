from collections import defaultdict
from collections import namedtuple
import sys
from icecream import ic
import networkx as nx
import matplotlib.pyplot as plt


filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)
ic(lines)
edges = [tuple(x.split("-")) for x in lines]
ic(edges)
g = nx.Graph()

g.add_edges_from(edges)
ic(g.number_of_nodes())

#nx.draw(g, with_labels=True, font_weight='bold')
#plt.show()

def findPathsFrom( g, path ):
    if path[-1] == 'end':
        return [ path ]
    tlc = False
    lcd = defaultdict(int)
    for n in path:
        if n.islower() and n != 'start':
           lcd[n] += 1
    #ic(lcd)
    tc = 0
    for v in lcd.values():
        if v ==2 and tc >= 1:
            return []
        if v > 2:
            tcl = True
            #ic("visited lower more than twice")
            return []
        if v == 2:
            tc += 1
    nextNodes = list(g.neighbors(path[-1]))
    if 'start' in nextNodes:
        nextNodes.remove('start')
    #ic(nextNodes)
    np = []
    for n in nextNodes:
        #ic(n,path)
        if (not n in path) or n.isupper() or (not tlc):
            nextp = path.copy()
            nextp.append(n)
            np.extend(findPathsFrom(g, nextp))
        else:
            pass
            #np.append(path)
    #ic("returning", np)
    return np

ipath = ['start']
paths = findPathsFrom( g, ipath )
ic(paths)
ic(len(paths))
