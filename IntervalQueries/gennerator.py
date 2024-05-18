import random
import math

def getInputListRandom(n: int, max: int, min: int):
    lst = list()
    for i in range(n):
        year = random.randint(min, max)
        rain = random.randint(i*100, max)
        lst.append((year, rain))
    
    l2 = sorted(lst, key=lambda tup: tup[0])
    return l2

def getInputListOrders(n: int, max_value: int, min_value: int):
    lst = list()
    start = int(n/2)*(-1)
    for i in range(n):
        rain = random.randint(min(i*100,(max_value-100)), max_value)
        lst.append((start, rain))

        chance = random.randint(1, 100)
        if chance > 95:
            start += 10
        else:
            start += 1
    
    l2 = sorted(lst, key=lambda tup: tup[0])
    return l2

def getWorstCase():
    lst = list()
    start = -50000
    max_value = int(math.pow(10,9))
    for i in range(50000):
        rain = random.randint(min(i*100,(max_value-100)), max_value)
        lst.append((start, rain))

        start += 2
    
    l2 = sorted(lst, key=lambda tup: tup[0])
    return l2

def printQueryToFile(n:int, s:str, lst: list):
    file = open(s, "w") 
    file.write(f"{n}\n")
    for x in lst:
        file.write(f"{x[0]} {x[1]}\n")
    queries = int(n*((n-1)*0.5)) 
    file.write(f"{queries}\n")
    for y in range(n-1):
        for z in range(n-y-1):
            file.write(f"{lst[y][0]} {lst[y+z+1][0]}\n")
    file.write("\n")
    file.write("0\n")
    file.write("0\n")
    file.close()
    
def printQueryToFile(s:str, lst: list):
    n = 50000
    file = open(s, "w") 
    file.write(f"{n}\n")
    for x in lst:
        file.write(f"{x[0]} {x[1]}\n")
        
    queries = int(10000) 
    file.write(f"{queries}\n")
    for y in range(queries):
        file.write(f"{lst[1][0]+1} {lst[len(lst)-2][0]-1}\n")
    file.write("\n")
    file.write("0\n")
    file.write("0\n")
    file.close()    


# max_ = int(math.pow(10,9))
# min_ = -1*max_
# n_ = 100
# sort1 = getInputListRandom(n=n_, max=max_, min=min_)
# printQueryToFile(n_, "3.in", sort1)


# n2_ = 20
# sort2 = getInputListOrders(n=n2_, max_value=max_, min_value=min_)
# printQueryToFile(n2_, "4.in", sort2)

sortWorst = getWorstCase()
printQueryToFile("worst.in", sortWorst)


