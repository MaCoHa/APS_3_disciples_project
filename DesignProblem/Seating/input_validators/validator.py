import sys
import re

try: 
    n = int(sys.stdin.readline())
    assert 100 >= n > 0
    for _ in range(n):
        l = sys.stdin.readline()
        assert re.match("(0|[1-9][0-9]*) ([1-9][0-9]*)", l) != None
    line = sys.stdin.readline()
    assert len(line) == 0

    sys.exit(42)
except ValueError:
    sys.exit(43)