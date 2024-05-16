from collections import defaultdict
from sys import stdin

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
             for i in range(-1,2):
                #print(i)
                for j in range(-1,2):
                    new_x_cord = x_cord+i
                    new_y_cord = y_cord+j
                    if i == 0 and j == 0:
                        continue
                    if (new_x_cord >= 0 and new_x_cord < w ) and (new_y_cord >= 0 and new_y_cord < h):
                        graph[(x_cord,y_cord,OUT)][(new_x_cord,new_y_cord, IN)] = 1

#Credit Riko: https://github.itu.dk/algorithms/aps-24/blob/main/060-network-flows/code/flow.py
def bfs(graph,src,dest,mincap=0):
    parent = {src:src}
    layer = [src]
    while layer:
        nextlayer = []
        for u in layer:
            for v,cap in graph[u].items():
                if cap > mincap and v not in parent:
                    parent[v] = u
                    nextlayer.append(v)
                    if v == dest:
                        p =  []
                        current_vertex = dest
                        while src != current_vertex:
                            p.append((parent[current_vertex],current_vertex))
                            current_vertex = parent[current_vertex]
                        return (True,p)
        layer = nextlayer
    return (False,set(parent))

def flow(orggraph, src,dest):
    graph = defaultdict(lambda: defaultdict(int))
    maxcapacity = 0
    for u,d in orggraph.items():
        for v,c in d.items():
            graph[u][v] = c
            maxcapacity = max(maxcapacity,c)

    current_flow = 0
    mincap = maxcapacity
    while True:
        ispath, p_or_seen = bfs(graph,src,dest,mincap)
        if not ispath:
            if mincap > 0:
                mincap = mincap // 2
                continue
            else:
                return (current_flow,
                        { a:{b:c-graph[a][b] for b,c in d.items() if graph[a][b]<c} 
                            for a,d in orggraph.items() },
                        p_or_seen)
        p = p_or_seen
        saturation = min( graph[u][v] for u,v in p )
        current_flow += saturation
        for u,v in p:
            graph[u][v] -= saturation
            graph[v][u] += saturation

currentFlow, newGraph, seen = flow(graph, source, sink)
queue = [source]
minCut = set()
while queue:
    node = queue.pop(0)

    for neighbor in newGraph[node]:
        if neighbor not in seen:
            minCut.add(neighbor)
        else:
            queue.append(neighbor)
        
print("G", currentFlow)
#for node in minCut:
    #(node[0], node[1])