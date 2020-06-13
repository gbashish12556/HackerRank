def noOfPairs(arrayA,arrayB,lenArrayA,lenArrayB):
    arrayA.sort(key=int)
    arrayB.sort(key=int)
    print(arrayA)
    print(arrayB)
    n = 0
    k = 0
    count = 0
    if arrayB[0] == 1:
        k = k+1
        if arrayA[0] == 1:
            n=n+1
            count = lenArrayA-1
        else:
            count = lenArrayA
    while n < lenArrayA and k < lenArrayB:
        if arrayA[n] < arrayB[k]:
            count = count+1
            n = n+1
        elif arrayA[n]  > arrayB[k]:
            k = k+1
    return count

testCases = int(input())
for n in range(testCases):
    len = list(map(int,input().split(" ")))
    lenArrayA,lenArrrayB = len[0],len[1]
    arrayA = list(map(int,input().split(" ")))
    arrayB = list(map(int, input().split(" ")))
    found = noOfPairs(arrayA,arrayB,lenArrayA,lenArrrayB)
    print(found)