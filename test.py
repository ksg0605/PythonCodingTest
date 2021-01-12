n, m, k = map(int, input().split())
numList = list(map(int, input().split()))
print(numList)
numList.sort(numList)
print(numList)
sum = 0
maxNum = 0
index = m//(k+1)
rest = m%(k+1)
if m%(k+1) == 0:
    sumNum = index * (k * numList[-1] + numList[-2])
else:
    sumNum = index * (k * numList[-1] + numList[-2]) + rest * n5umList[-1]
print(sumNum)