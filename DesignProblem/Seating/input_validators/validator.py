#!/usr/bin/env python3

import sys

try: 
    w,h = map(int, sys.stdin.readline().split())
    assert 300 >= w > 2
    assert 300 >= h > 2
    sources = 0
    sinks = 0
    free = 0
    lines = sys.stdin.readlines();
    assert len(lines) == h
    for rawLine in lines:
        line = rawLine.split()
        assert len(line) == w
        for char in line:
            assert char in ["0", "S", "I", "H"]
            if char == "0":
                free += 1
            elif char == "S":
                sinks += 1
            elif char == "I":
                sources += 1
    assert sources >= 1
    assert sinks >= 1
    assert free >= 1
    sys.exit(42)
except ValueError:
    sys.exit(43)