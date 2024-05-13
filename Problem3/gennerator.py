import random
import math

def getInputList(n: int, max: int, min: int):
    lst = list()
    for i in range(n):
        year = random.randint(min, max)
        rain = random.randint(i*100, max)
        lst.append((year, rain))
    
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

def createResults(lst:list):
    result = list()
    #TODO get a solution from the internet
    return result

def printAnswerToFile(lst:list, s:str):
    file = open(s, "w") 
    for x in lst:
        file.write(f"{x}\n")
    file.close()
    

lst = list()
max_ = int(math.pow(10,9))
min_ = -1*max_
n_ = 20

sort1 = getInputList(n=n_, max=max_, min=min_)
printQueryToFile(n_, "3.in", sort1)
res1 = createResults(sort1)
printAnswerToFile(res1, "3.ans")

# lst = list()
# n_ = 20
# sort2 = getInputList(n=n_, max=max_, min=min_)
# printQueryToFile(n_, "4.in", sort2)
# res2 = createResults(sort2)
# printAnswerToFile(res2, "4.ans")


