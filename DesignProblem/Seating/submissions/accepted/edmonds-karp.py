



from collections import defaultdict
from sys import stdin


def bfs ():
    print("bfs")
    
    
def flow():
    print("flow")
    


source = "source"
sink = "sink"
maxcap = 1

x, y = map(int,next(stdin).split())

dict = defaultdict(lambda: defaultdict(int))
# I == sources
# S == sinks
# H == Wall
# 0 == open

for x_cord in range(x):
    list = (next(stdin).split())
    for y_cord, j in enumerate(list):
        print(x_cord,y_cord,j)
        if (j == "I"):
            dict[source][(x_cord,y_cord)] = 10
            
        elif (j == "S"):
            dict[(x_cord,y_cord)][sink] = 10
           
        if (j != "H"):
             for i in range(-1,2):
                print(i)
                for j in range(-1,2):
                    new_x_cord = x_cord+i
                    new_y_cord = y_cord+j
                    if i == 0 and j == 0:
                        continue
                    if (new_x_cord >= 0 and new_x_cord < x ) and (new_y_cord >= 0 and new_y_cord < y):
                        dict[(x_cord,y_cord)][new_x_cord,new_y_cord] = maxcap

        
       