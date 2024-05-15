from collections import defaultdict
from sys import stdin

IN = 0
OUT = 1
source = "source"
sink = "sink"
maxcapacity = 10

w, h = map(int, next(stdin).split())
graph = defaultdict(lambda: defaultdict(int))

for y_cord in range(h):
    lst = next(stdin).split()
    for x_cord, j in enumerate(lst):
        if j == "I":
            graph[source][(x_cord, y_cord, OUT)] = maxcapacity
        elif j == "S":
            graph[(x_cord, y_cord, IN)][sink] = maxcapacity
        if j != "H":
            if j != "S" and j != "I":
                graph[(x_cord, y_cord, IN)][(x_cord, y_cord, OUT)] = maxcapacity if j == "I" or j == "S" else 1
            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_x_cord = x_cord + i
                    new_y_cord = y_cord + j
                    if i == 0 and j == 0:
                        continue
                    if 0 <= new_x_cord < w and 0 <= new_y_cord < h:
                        graph[(x_cord, y_cord, OUT)][(new_x_cord, new_y_cord, IN)] = 1
                        
