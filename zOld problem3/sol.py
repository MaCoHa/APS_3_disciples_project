#https://open.kattis.com/problems/workout?tab=metadata
import math

#Takes all jims workout and rest times.
JimsTimes = [*map(int, input().split())]

#Split them in thier own arrays
jWork = JimsTimes[::2]
jRest = JimsTimes[1::2]

#Start time
t = 0

#Others workout and rest times
oWork = []
oRest = []
oNextUseT = []

#Whis can be done i a one liner.                 #oWork, oRest, oStartT = map(list, zip(*([*map(int, input().split())] for _ in range(10))))
for _ in range(10):
    x = list(map(int, input().split()))
    oWork.append(x[0]); oRest.append(x[1]), oNextUseT.append(x[2])

oNextFreeT = [0]*10

#He does the 10 machine sequence 3 times.
for _ in range(3):
    for i in range(10):

        #Jim will back down in a tie 
        aviable = t < oNextUseT[i]

        if not aviable:
            oNextUseT[i] += (oWork[i]+oRest[i]) * (1+math.floor((t-oNextUseT[i])/(oWork[i]+oRest[i])))#(t-oNextUseT[i])+(t-oNextUseT[i])%(oWork[i]+oRest[i])
            oNextFreeT[i] = oNextUseT[i]-oRest[i]
        
        #print(f"t:{t} - oNextFree:{oNextFreeT[i]} - oNextUse:{oNextUseT[i]}")
        
        t = max(t, oNextFreeT[i])+jWork[i]+jRest[i]
        oNextUseT[i] = max(t-jRest[i], oNextUseT[i])
        oNextFreeT[i] = t - jRest[i]

print(t-jRest[-1])
















# ur = [*map(int, input().split())]
# u = ur[::2]; r = ur[1::2]; t = 0
# uu, rr, tt = map(list, zip(*([*map(int, input().split())] for _ in range(10)))); ss = tt.copy()
# # tt[i]: when's the next available time for machine i
# for _ in range(3):
#     for i in range(10):
#         start = t >= ss[i]
#         if start: # update machine's next available time
#             tt[i] = t-(t-max(tt[i], ss[i]))%(uu[i]+rr[i])
#             nn = tt[i]+uu[i]+rr[i] # incorporate recovery time of person i
#             tt[i] = max(tt[i]+uu[i], t) # see if person i can do one more rep
#         if not start or t > tt[i]: t += u[i]; tt[i] = t
#         else: t = tt[i] + u[i]; tt[i] = t
#         t += r[i]
#         if start: tt[i] = max(tt[i], nn)
# print(t-r[-1])