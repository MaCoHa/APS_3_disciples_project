#https://open.kattis.com/problems/worstweather?tab=metadata



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
        middle, noSkips = self.__bottom_up_range_Max(i+1, j-1)

        queryHolds = lower[0] >= upper[0] and upper[0] > middle

        if not queryHolds:
            return "false"
        elif noSkips:
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
    l = 0
    r = len(arr)-1

    if x > arr[r]:
        return arr[r]
    if x < arr[l]:
        return arr[l]

    while l < r:
        mid = (l + 1) + r // 2
        if arr[mid] == x:
            return arr[mid]
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    if findFloor:
        return arr[r]
    else:
        return arr[l]



while True:
    n = int(input())
    if n == 0:
        exit()
    
    bsArray =  [0] * n
    rainArray = [-1] * (n*2)
    dYearsIndexes = dict()
    nSkips = 0

    #First Year
    fYear, fRain = map(int, input().split())
    lastYear = fYear
    bsArray[0] = fYear
    rainArray[0] = fRain
    dYearsIndexes.update({fYear: 0})

    #Reading Years and info
    for i in range(n-1):
        iYear, iRain = map(int, input().split())
        
        bsArray[i+1] = iYear
        
        if lastYear != iYear-1:
            nSkips += 1
            rainArray[i+1+nSkips] = iRain
            dYearsIndexes.update({iYear: i+1+nSkips})
        else:
            rainArray[i+1] = iRain
            dYearsIndexes.update({iYear: i+1})

        lastYear = iYear

    sgTree = SegmentTree(nSkips+n)
    for x in range(nSkips+n):
        sgTree.update(x, rainArray[x])


    m = int(input())
    for _ in range(m):
        y, x = map(int, input().split())

        if y<bsArray[0] and x>bsArray[-1]:
            print("maybe")
            continue
        
        if y not in dYearsIndexes:
            y = dYearsIndexes.get(findClosestSearch(bsArray, y, False))
        else: 
            y = dYearsIndexes.get(y)
        
        if x not in dYearsIndexes:
            x = dYearsIndexes.get(findClosestSearch(bsArray, x, True))
        else: 
            x = dYearsIndexes.get(x)

        if x==y:
            print("maybe")
            continue

        print(sgTree.query(y,x))

    print("")
    input()








