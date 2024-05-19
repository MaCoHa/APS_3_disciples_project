#!/usr/bin/env python3
from collections import defaultdict
from sys import stdin

IN = 0
OUT = 1
source = "source"
sink = "sink"
maxcapacity = 8

w, h = map(int, next(stdin).split())
graph = defaultdict(lambda: defaultdict(int))

for y_cord in range(h):
    lst = next(stdin).split()
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
                        
def BFS(graph, s,t):
    visited = set()
    queue = [(s, [s], maxcapacity)]
    visited.add(s)
    while queue:
        (node, curPath, curFlow) = queue.pop(0)
        for neighbour, capacity in graph[node].items():
            if neighbour not in visited and capacity > 0:
                flow = min(capacity, curFlow)
                
                visited.add(neighbour)
                queue.append((neighbour, curPath + [neighbour], flow))
                if neighbour == t:
                    return curPath + [neighbour], flow, visited
    return [], 0, visited


def flow(graph, source, sink):
    total_flow = 0
    path, flow, visited = BFS(graph, source, sink)
    while path:
        total_flow += flow
        graph = augment(graph, path, flow)
        path, flow, visited = BFS(graph, source, sink)
    minCut = set()
    for u in visited:
        for v,cap in graph[u].items():
            if v not in visited and cap == 0:
                if u[2] == IN:    
                    if u[0] == v[0] and u[1] == v[1]:
                        minCut.add((v[0],v[1]))
                else:
                    minCut.add((v[0],v[1]))
    return total_flow, minCut

def augment(graph, path, flow):
    for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            graph[u][v] -= flow
            graph[v][u] += flow
    return graph

totalFlow, minCut = flow(graph, source, sink)

print("G", totalFlow)
for x, y in minCut:
    print(x, y)