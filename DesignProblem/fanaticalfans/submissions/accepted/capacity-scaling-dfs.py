#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin
import sys

IN = 0
OUT = 1
source = "source"
sink = "sink"
maxcapacity = 8

w, h = map(int, next(stdin).split())
graph = defaultdict(lambda: defaultdict(int))

for y_cord in range(h):
    l = next(stdin)
    lst = l.split()
    for x_cord, j in enumerate(lst):
        if j == "B":
            graph[source][(x_cord, y_cord, OUT)] = maxcapacity+1
        elif j == "F":
            graph[(x_cord, y_cord, IN)][sink] = maxcapacity
        if j != "H":
            if j != "F" and j != "B":
                graph[(x_cord, y_cord, IN)][(x_cord, y_cord, OUT)] = 1
            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_x_cord = x_cord + i
                    new_y_cord = y_cord + j
                    if i == 0 and j == 0:
                        continue
                    if 0 <= new_x_cord < w and 0 <= new_y_cord < h:
                        graph[(x_cord, y_cord, OUT)][(new_x_cord, new_y_cord, IN)] = 1
 
def dfs(graph,u,dest,mincap): # returns path to dest
    global seen
    stack = [(True,u)]
    path = []
    while stack:
        is_v,u_or_edges = stack.pop()
        if is_v:
            u = u_or_edges
            if u in seen:
                continue
            seen.add(u)
            if u == dest:
                return path[::-1]
            stack.append((False,[(u,v) 
                    for v,cap in graph[u].items()
                    if cap > mincap] ))
            path.append(None)
        else:
            path.pop()
            if u_or_edges:
                # print(u_or_edges)
                u_v = u_or_edges.pop()
                path.append(u_v)
                # print(u_v)
                u,v = u_v
                stack.append((False,u_or_edges))
                stack.append((True,v))
    return None

def flow(graph, src,dest):
    # we modify graph, it is the residual network
    global seen
    current_flow = 0
    mincap = maxcapacity
    while True:
        seen = set()
        p = dfs(graph,src,dest,mincap)
        if p == None:
            if mincap > 0:
                mincap = int(mincap*.5)
                continue
            else:
                return current_flow,graph,seen
        saturation = min( graph[u][v] for u,v in p )
        for i in range(len(p)-1):
            assert(p[i][0] == p[i+1][1])
        current_flow += saturation
        for u,v in p:
            graph[u][v] -= saturation
            graph[v][u] += saturation
            
currentFlow, newGraph, seen = flow(graph,source,sink)
queue = [source]
minCut = set()
for u in seen:
    for v,cap in newGraph[u].items():
        if v not in seen and cap == 0:
            if u[2] == IN:    
                if u[0] == v[0] and u[1] == v[1]:
                    minCut.add((v[0],v[1]))
            else:
                minCut.add((v[0],v[1]))

#print(seen)
print("G", currentFlow)
for x,y in minCut:
    print(x,y)
