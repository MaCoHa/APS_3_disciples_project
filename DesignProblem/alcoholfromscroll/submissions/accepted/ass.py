nDrinks = int(input())

bestDrinkIndex = -1
bestRatio = 0.0
for x in range(nDrinks):
    OH, price = map(int, input().split())
    ratio = OH/price
    if ratio > bestRatio:
        bestRatio = ratio
        bestDrinkIndex = x

print(bestDrinkIndex)