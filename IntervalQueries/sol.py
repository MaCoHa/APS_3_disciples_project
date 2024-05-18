#https://open.kattis.com/problems/worstweather?tab=metadata

import math
import sys

class SegmentTree():
    def __init__(self, n):
        self.N = 1
        while self.N < n:
            self.N *= 2
        self.A = [(0, False) for _ in range(2 * self.N)]

    def get(self, i):
        return self.A[self.N + i]
    
    def set(self, i, k):
        p = self.N + i
        self.A[p] = (k, k>0)

    def updateAll(self):
        p = self.N
        p //= 2
        while p > 0:
            x = 0 
            while x < p:
                i = p+x
                self.A[i] = (max(self.A[2 * (i)][0], self.A[2 * i + 1][0]), (self.A[2 * i][1] and self.A[2 * i + 1][1]))
                x += 1
            p //= 2
        
    #NOT used
    def update(self, i, k):
        p = self.N + i
        self.A[p] = (k, k>0)
        p //= 2
        while p > 0:
            self.A[p] = (max(self.A[2 * p][0], self.A[2 * p + 1][0]), (self.A[2 * p][1] and self.A[2 * p + 1][1]))
            p //= 2
    
    def query(self, i, j):
        lower = self.get(i)
        upper = self.get(j)
        if lower[0] == -1 and upper[0] == -1:
            return "maybe"
        
        isLowerAndUpperKnown = lower[0]>0 and upper[0]>0
        if lower[0] == -1:
            lower = upper
        if upper[0] == -1:
            upper = lower

        middle, noSkipsInbetween = self.__bottom_up_range_Max(i+1, j-1)

        queryHolds = lower[0] >= upper[0] and upper[0] > middle

        if not queryHolds:
            return "false"
        elif isLowerAndUpperKnown and noSkipsInbetween:
            return "true"
        else:
            return "maybe"

    def __bottom_up_range_Max(self, i, j):
        i += self.N
        j += self.N

        noSkips = True
        s = 0
        while i <= j:
            if i % 2 == 1:
                s = max(self.A[i][0],s)
                noSkips = noSkips and self.A[i][1]
                i += 1
            if j % 2 == 0:
                s = max(self.A[j][0],s)
                noSkips = noSkips and self.A[j][1]
                j -= 1
            i //= 2
            j //= 2
        return (s,noSkips)


def findClosestSearch(arr: list, x, findFloor: bool):
    lowerBound = 0
    higherBound = len(arr)-1
    
    if x > arr[higherBound]:
        return arr[higherBound]
    if x < arr[lowerBound]:
        return arr[lowerBound]

    while lowerBound <= higherBound: #Potentially flips lower and higher
        mid = lowerBound + (higherBound-lowerBound) // 2
        if arr[mid] == x:   #will never happen
            return arr[mid]
        if arr[mid] < x:
            lowerBound = mid + 1
        else:
            higherBound = mid - 1
    if findFloor: #higher and lower are maybe fliped at the end.
        if arr[higherBound] < x:
            return arr[higherBound]
        else:
            return arr[min(higherBound-1,0)]
    else:
        if arr[lowerBound] > x:
            return arr[lowerBound]
        else:
            return arr[max(lowerBound+1,len(arr)-1)]


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        exit()
    
    binarysearchArray =  [0] * (n)
    rainArray = [-1] * ((n*2)+1)
    dYearsIndexes = dict()
    nSkips = 0 
    previousYear = -1*math.pow(10,9)

    #Reading Years and info
    for i in range(n):
        iYear, iRain = map(int, sys.stdin.readline().split())
        binarysearchArray[i] = iYear
        if previousYear != iYear-1:
            nSkips += 1
        rainArray[i+nSkips] = iRain
        dYearsIndexes.update({iYear: i+nSkips})
        previousYear = iYear

    #Update SegmentTree based on rain data
    sgTree = SegmentTree(nSkips+n+1)
    for xx in range(nSkips+n+1):
        sgTree.set(xx, rainArray[xx])
    sgTree.updateAll()

    #Search through 
    m = int(sys.stdin.readline())
    for _ in range(m):
        startYear, endYear = map(int, sys.stdin.readline().split())
        startYearIndex = -1
        endYearIndex = -1

        #Checks if the hole range is outside the given data.
        if startYear > binarysearchArray[-1] or endYear < binarysearchArray[0]:
            print("maybe")
            continue

        #Finding index for startYear or the closes index we have data for. 
        if startYear not in dYearsIndexes:
            startYearIndex = dYearsIndexes.get(findClosestSearch(binarysearchArray, startYear, False))-1
        else: 
            startYearIndex = dYearsIndexes.get(startYear)
        
        #Finding index for startYear or the closes index we have data for. 
        if endYear not in dYearsIndexes:
            endYearIndex = dYearsIndexes.get(findClosestSearch(binarysearchArray, endYear, True))+1 #The +1 is the get the index of the skip where endyear belong
        else: 
            endYearIndex = dYearsIndexes.get(endYear)
        
        #Prints the result of query
        print(sgTree.query(startYearIndex,endYearIndex))

    print("") #print empty line
    sys.stdin.readline()







