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
        if (j == "I"):
            graph[source][(x_cord,y_cord, IN)] = maxcap
            
        elif (j == "S"):
            graph[(x_cord,y_cord,IN)][sink] = maxcap
           
        if (j != "H"):
             graph[(x_cord,y_cord,IN)][(x_cord,y_cord,OUT)] = maxcap if j == "I" or j == "S" else 1
             for i in range(-1,2):
                #print(i)
                for j in range(-1,2):
                    new_x_cord = x_cord+i
                    new_y_cord = y_cord+j
                    if i == 0 and j == 0:
                        continue
                    if (new_x_cord >= 0 and new_x_cord < w ) and (new_y_cord >= 0 and new_y_cord < h):
                        graph[(x_cord,y_cord,OUT)][(new_x_cord,new_y_cord, IN)] = 1

def bfs(graph):
    queue = [(source, [source], float("inf"))]
    visited = [source]
    
    while queue:
        node, path, cur_flow = queue.pop(0)
        adj_nodes = graph[node]
        for adj_node, capacity in adj_nodes.items():
            if adj_node not in visited and capacity > 0:
                flow = min(capacity, cur_flow)
                queue.append((adj_node, path + [adj_node], flow))
                visited.append(adj_node)

                if adj_node == sink:
                    return path + [sink], flow
    
    return ([], 0)

def flow(orggraph):
    
    current_flow = 0
    graph = defaultdict(lambda: defaultdict(int))
    for u,d in orggraph.items():
        for v,c in d.items():
            graph[u][v] = c
    while True:
        path, curFlow = bfs(graph)
        current_flow += curFlow
        if not path:
            return (current_flow,
                        { a:{b:c-graph[a][b] for b,c in d.items() if graph[a][b]<c} 
                            for a,d in orggraph.items() },
                        path)
        #saturation = min( graph[u][v] for u,v in path )
        
        for i in range(len(path)-1):
            u,v = path[i], path[i+1]
            graph[u][v] -= curFlow
            graph[v][u] += curFlow

currentFlow, newGraph, seen = flow(graph)
queue = [source]
minCut = set()
while queue:
    node = queue.pop(0)

    for neighbor in newGraph[node]:
        if neighbor not in seen:
            minCut.add(neighbor)
        else:
            queue.append(neighbor)
print("F", currentFlow)
for node in minCut:
    print(node[0], node[1])