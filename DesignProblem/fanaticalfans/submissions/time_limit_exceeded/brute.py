#!/usr/bin/env python3
from collections import defaultdict
from sys import stdin
from itertools import combinations
IN = 0
OUT = 1
source = "source"
sink = "sink"
maxcap = 10

w, h = map(int,next(stdin).split())
graph = defaultdict(lambda: defaultdict(int))
# I == sources
# S == sinks
# H == Wall
# 0 == open

# Node (x,y,IN) is the node that represents the incoming edge to the cell (x,y)
# Node (x,y,OUT) is the node that represents the outgoing edge from the cell (x,y)

possible_gaurd_places = []

for y_cord in range(h):
    list = (next(stdin).split())
    for x_cord, j in enumerate(list):
        #print(x_cord,y_cord,j)
        if (j == "B"):
            graph[source][(x_cord,y_cord, IN)] = maxcap
            
        elif (j == "F"):
            graph[(x_cord,y_cord,IN)][sink] = maxcap
           
        if (j != "H"):
             graph[(x_cord,y_cord,IN)][(x_cord,y_cord,OUT)] = maxcap if j == "B" or j == "F" else 1
             if j == "0":
                possible_gaurd_places.append((x_cord,y_cord))
             for i in range(-1,2):
                #print(i)
                for j in range(-1,2):
                    new_x_cord = x_cord+i
                    new_y_cord = y_cord+j
                    if i == 0 and j == 0:
                        continue
                    if (new_x_cord >= 0 and new_x_cord < w ) and (new_y_cord >= 0 and new_y_cord < h):
                        graph[(x_cord,y_cord,OUT)][(new_x_cord,new_y_cord, IN)] = 1

k = 1


def BFS(graph, s,t, removedNodes):
    visited = set()
    queue = [(s, [s])]
    visited.add(s)
    while queue:
        (node, curPath) = queue.pop(0)
        for neighbour, capacity in graph[node].items():
            if neighbour not in visited and capacity > 0 and neighbour not in removedNodes:
                visited.add(neighbour)
                queue.append((neighbour, curPath + [neighbour]))
                if neighbour == t:
                    return True
    return False
pathFound = True
while pathFound or k >= len(possible_gaurd_places):
    for combies in combinations(possible_gaurd_places, k):
        removedNodes = set()
        for comb in combies:
            removedNodes.add((comb[0],comb[1],IN))
            removedNodes.add((comb[0],comb[1],OUT))
        pathFound = BFS(graph, source, sink, removedNodes)
        if not pathFound:
            print("G",k)
            for comb in combies:
                print(comb[0],comb[1])
            break
    
    k += 1
    if k == 1000:
        break
            
            