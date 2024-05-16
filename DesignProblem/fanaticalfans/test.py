import sys


_, n = input().split()

f = open("tmp.txt", "r")
print(f.read())

lines = sys.stdin.readlines();
coords = set()
for line in lines:
    if line not in coords:
        coords.add(line)
    else:
        print("NO")
        print(line)
#print(coords)