
from collections import defaultdict
from sys import stdin
import sys

IN = 0
OUT = 1
source = "source"
sink = "sink"
maxcap = 10
maxcapacity = 10

w, h = map(int, next(stdin).split())
graph = defaultdict(lambda: defaultdict(int))

for y_cord in range(h):
    lst = next(stdin).split()
    for x_cord, j in enumerate(lst):
        if j == "B":
            graph[source][(x_cord, y_cord, IN)] = maxcap
        elif j == "F":
            graph[(x_cord, y_cord, IN)][sink] = maxcap
            #graph[(x_cord, y_cord, IN)][(x_cord, y_cord, OUT)] = maxcap

        if j != "H":
            if j != "F":
                graph[(x_cord, y_cord, IN)][(x_cord, y_cord, OUT)] = maxcap if j == "B" or j == "F" else 1
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
    if u in seen:
        return None
    seen.add(u)
    for v,cap in graph[u].items():
        if cap > mincap:
            if v == dest:
                return [(u,v)]
            # print(f'explore {u} {v}, {cap}')
            p = dfs(graph,v,dest,mincap)
            if p:
                p.append((u,v))
                return p
    return None

def dfs_it(graph,u,dest,mincap): # returns path to dest
    global seen
    stack = [(True,u)]
    path = []
    while stack:
        # print(stack)
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
                    #sorted(graph[u].items(),key=lambda x:-x[1]) 
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

def bfs(graph,src,dest,mincap): # returns path to dest
    global seen
    parent = dict()
    layer = [src]
    while layer:
        nextlayer = []
        for u in layer:
            seen.add(u)
            for v,cap in graph[u].items():
                if cap > mincap and v != src and v not in parent:
                    parent[v] = u
                    nextlayer.append(v)
                    if v == dest:
                        p =  []
                        prev = dest
                        while prev in parent:
                            p.append((parent[prev],prev))
                            prev = parent[prev]
                        return p
        layer = nextlayer
    return None

def flow(graph, src,dest):
    # we modify graph, it is the residual network
    global seen
    current_flow = 0
    mincap = maxcapacity
    while True:
        seen = set()
        p = dfs_it(graph,src,dest,mincap)
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
counter = 0
seen_nodes = set()
while queue:
    
    node = queue.pop(0)

    for neighbor in newGraph[node]:
        if neighbor not in seen:
            minCut.add(neighbor)
        elif neighbor not in seen_nodes:
            queue.append(neighbor)
    seen_nodes.add(node)

print("G", currentFlow)
for node in minCut:
    print(node[0], node[1])
