

testCases = int(input())
for n in range(testCases):
    listA = list(map(int,input().split(" ")))
    lenListA = len(listA)
    sumValue = int(input())
    sumMatrix = [[0 for n in range(sumValue+1)] for k in range(lenListA)]
    for x in range(lenListA):
        sumMatrix[x][0] = 1
    for x in range(lenListA):
        for k in range(1,sumValue+1):
            if k == listA[x]:
                sumMatrix[x][k] = 1
            elif k > listA[x] and x > 0:
                sumMatrix[x][k] = sumMatrix[x-1][k-listA[x]]
            else:
                sumMatrix[x][k] = sumMatrix[x-1][k]
    print(sumMatrix[lenListA-1][sumValue])