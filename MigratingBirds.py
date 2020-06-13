from collections import defaultdict

def migratoryBirds(arr,newSet):
    newSet.sort()

    dictArray = defaultdict()
    maxCount = 0

    lenArray = len(arr)
    lenSet = len(newSet)
    key = 0

    for i in range(lenSet):
        dictArray[newSet[i]] = 0

    for i in range(lenArray):
        dictArray[arr[i]] += 1

    for x in newSet:
        if dictArray[x] > maxCount:
            maxCount  = dictArray[x]
            key = x

    return key

testCases = int(input())
for n in range(testCases):

    array = list(map(int,input().split(" ")))
    newSet = list(set(array))

    print(migratoryBirds(array,newSet))