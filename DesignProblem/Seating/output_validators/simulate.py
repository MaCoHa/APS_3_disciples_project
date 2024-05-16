#!/usr/bin/env python3

from collections import defaultdict
import re

""" Check the output

    Typically run by verifyproblem. To run on its own from the command line,
    invoke as

    > ./validate.py input_file.in judge_answer.ans feedback_dir < team_answer.ans

    feedback_dir must exist
"""

import sys
from pathlib import Path

feedback_dir = sys.argv[3]

def fail(msg: str) -> None:
    """Fail WA with given message"""
    with open(feedback_dir / Path("judgemessage.txt"), "a", encoding="utf-8") as jfile:
        jfile.write(f"WA: {msg}\n")
    with open(feedback_dir / Path("teammessage.txt"), "a", encoding="utf-8") as afile:
        afile.write(f"WA: {msg}\n")
    print(msg, file=sys.stderr)
    sys.exit(43)


def accept() -> None:
    sys.exit(42)


def get_team_answer():
    team_bytes = sys.stdin.buffer.read()
    try:
        team_lines = team_bytes.decode("utf-8").splitlines()
    except UnicodeDecodeError:
        fail("Team answer contains unexpected characters")
    if not team_lines:
        fail("Submission produces empty output")
    return team_lines

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


with open(sys.argv[1]) as in_file, open(sys.argv[2]) as ans_file:
    graph = defaultdict(lambda: defaultdict(int))
    
    stadium = [l.split() for l in in_file.readlines()[1:]]
    for y in range(len(stadium)):
        for x in range(len(stadium[y])):
            if stadium[y][x] == "B":
                graph[source][(x, y)] = maxcap
            elif stadium[y][x] == "F":
                graph[(x, y)][sink] = maxcap
            if stadium[y][x] != "H":
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        new_x = x + i
                        new_y = y + j
                        if i == 0 and j == 0:
                            continue
                        if 0 <= new_x < len(stadium[0]) and 0 <= new_y < len(stadium):
                            graph[(x, y)][(new_x, new_y)] = 1
    #print(bfs(graph, source, sink))
    answer = get_team_answer()
    if len(answer) == 0:
        fail("Output can not be empty")
    jury_answer = ans_file.readlines()
    first_line = answer[0].split()
    if len(first_line) != 2 or first_line[0] != "G":
        fail("Invalid first line")
    
    if len(answer) != int(first_line[1]) + 1:
        fail("Invalid number of lines")
    if jury_answer[0].split()[1] != first_line[1]:
        fail("Incorrent flow level")
    guards = 0
    for line in answer[1:]:
        guards += 1
        if re.match("(0|[1-9][0-9]*) (0|[1-9][0-9]*)", line) == None:
            fail("Invalid line")
        x, y = map(int, line.split())
        if stadium[y][x] == "H":
            fail("Can not place gaurd at a wall")
        if stadium[y][x] == "B":
            fail("Can not place gaurd at a source")
        if stadium[y][x] == "F":
            fail("Can not place gaurd at a sink")
        if (x, y) in graph[source]:
            fail("Can not place gaurd at a source")
        if (x, y) in graph[sink]:
            fail("Can not place gaurd at a sink")
        if (x, y) not in graph:
            fail("Can not place gaurd outside stadium")
        graph.pop((x, y))
    if guards != int(first_line[1]):
        fail("Invalid number of guards")
    if bfs(graph, source, sink):
        fail("Fans can still reach the sink")
        
    accept()
