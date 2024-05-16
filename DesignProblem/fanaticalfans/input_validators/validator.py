#!/usr/bin/env python3

import sys

try: 
    w,h = map(int, sys.stdin.readline().split())
    assert 300 >= w >= 2
    assert 300 >= h >= 2
    sources = set()
    sinks = set()
    free = 0
    lines = sys.stdin.readlines();
    assert len(lines) == h
    x = 0
    for rawLine in lines:
        line = rawLine.split()
        assert len(line) == w
        y = 0
        for char in line:
            assert char in ["0", "F", "B", "H"]
            if char == "0":
                free += 1
            elif char == "F":
                sinks.add((x, y))
            elif char == "B":
                sources.add((x, y))
            y += 1
        x += 1
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
    sys.exit(42)
except ValueError:
    sys.exit(43)