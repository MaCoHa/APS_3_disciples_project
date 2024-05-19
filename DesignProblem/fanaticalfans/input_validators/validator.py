#!/usr/bin/env python3

from collections import defaultdict
import sys

source = "source"
sink = "sink"
maxcap = 10
def bfs(graph,src,dest):
    parent = {src:src}
    layer = [src]
    while layer:
        nextlayer = []
        for u in layer:
            for v,_ in graph[u].items():
                if v not in parent:
                    parent[v] = u
                    nextlayer.append(v)
                    if v == dest:
                        p =  []
                        current_vertex = dest
                        while src != current_vertex:
                            p.append((parent[current_vertex],current_vertex))
                            current_vertex = parent[current_vertex]
                        return True
        layer = nextlayer
    return False

try: 
    graph = defaultdict(lambda: defaultdict(int))
    w,h = map(int, sys.stdin.readline().split())
    assert 30 >= w >= 2
    assert 30 >= h >= 2
    sources = set()
    sinks = set()
    free = 0
    lines = sys.stdin.readlines();
    assert len(lines) == h
    y = 0
    for rawLine in lines:
        line = rawLine.split()
        assert len(line) == w
        x = 0
        for char in line:
            assert char in ["0", "F", "B", "H"]
            if char == "0":
                free += 1
            elif char == "F":
                sinks.add((x, y))
                graph[(x, y)][sink] = maxcap
            elif char == "B":
                sources.add((x, y))
                graph[source][(x, y)] = maxcap
            if char != "H":
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        new_x = x + i
                        new_y = y + j
                        if i == 0 and j == 0:
                            continue
                        if 0 <= new_x < w and 0 <= new_y < h:
                            graph[(x, y)][(new_x, new_y)] = 1
            x += 1
        y += 1
    assert len(sources) >= 1
    assert len(sinks) >= 1
    assert free >= 1
    for (x,y) in sources:
        assert (x,y) not in sinks
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0:
                    continue
                if x+i >= 0 and x+i < w and y+j >= 0 and y+j < h:
                    assert (x+i, y+j) not in sinks
    assert bfs(graph, source, sink)
    sys.exit(42)
except ValueError:
    sys.exit(43)