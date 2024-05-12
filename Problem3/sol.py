#https://open.kattis.com/problems/worstweather?tab=metadata

import math

class SegmentTree():
    def __init__(self, n):
        self.N = 1
        while self.N < n:
            self.N *= 2
        self.A = [(0, False) for _ in range(2 * self.N)]

    def get(self, i):
        return self.A[self.N + i]
    
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
    
    if x > arr[higherBound-1]:
        return arr[higherBound]
    if x < arr[lowerBound+1]:
        return arr[lowerBound]

    while lowerBound <= higherBound: #Flips lower and higher
        mid = lowerBound + (higherBound-lowerBound) // 2
        if arr[mid] == x:   #propperly will never happen
            return arr[mid]
        if arr[mid] < x:
            lowerBound = mid + 1
        else:
            higherBound = mid - 1
    if findFloor: #higher and lower are fliped at the end.
        return arr[higherBound]
    else:
        return arr[lowerBound]



while True:
    n = int(input())
    if n == 0:
        exit()
    
    bsArray =  [0] * (n)
    rainArray = [-1] * ((n*2)+2)
    dYearsIndexes = dict()
    nSkips = 0 #starts with a skip

    #Reading Years and info
    fYear, fRain = map(int, input().split())
    bsArray[0] = fYear
    rainArray[1] = fRain #We make room for a skip
    dYearsIndexes.update({fYear: 1})
    lastYear = fYear
    for i in range(n-1):
        iYear, iRain = map(int, input().split())
        bsArray[i+1] = iYear #+1 because of first read
        if lastYear != iYear-1:
            nSkips += 1
        rainArray[i+2+nSkips] = iRain #+2 because of first read and first skip
        dYearsIndexes.update({iYear: i+2+nSkips})
        lastYear = iYear

    #Update SegmentTree based on rain data
    sgTree = SegmentTree(nSkips+n+2)
    for xx in range(nSkips+n+2):
        sgTree.update(xx, rainArray[xx])

    #Search through 
    m = int(input())
    for _ in range(m):
        startYear, endYear = map(int, input().split())
        startYearIndex = -1
        endYearIndex = -1

        if startYear > bsArray[-1] or endYear < bsArray[0]:
            print("maybe")
            continue

        if startYear not in dYearsIndexes:
            if startYear < bsArray[0]:
                startYearIndex = 0
            else:
                startYearIndex = dYearsIndexes.get(findClosestSearch(bsArray, startYear, False))-1
        else: 
            startYearIndex = dYearsIndexes.get(startYear)
        
        
        if endYear not in dYearsIndexes:
            if endYear > bsArray[-1]:
                endYearIndex = nSkips+n+1
            endYearIndex = dYearsIndexes.get(findClosestSearch(bsArray, endYear, True))+1
        else: 
            endYearIndex = dYearsIndexes.get(endYear)


        # if startYear==-944600985 and endYear ==-736167351:
        #     print("##############")
        #     print(bsArray)
        #     print(rainArray)
        #     #print(dYearsIndexes)
        #     print(f"{findClosestSearch(bsArray, startYear, False)}, {findClosestSearch(bsArray, endYear, True)}")
        #     print(f"{startYearIndex}, {endYearIndex}")

        #     max_ = 0
        #     mIndex = 0

        #     for x in range(endYearIndex-startYearIndex):
        #         if rainArray[x+startYearIndex] > max_:
        #             #print(rainArray[x+startYearIndex])
        #             max_ = rainArray[x+startYearIndex]
        #             mIndex = x+startYearIndex
        #     print(f"index:{mIndex}, max:{max_}")

        
        print(sgTree.query(startYearIndex,endYearIndex))

    print("") #print empty line
    input()








