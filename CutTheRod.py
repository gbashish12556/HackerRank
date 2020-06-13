

testCases = int(input())
for n in range(testCases):
    listA = list(map(int,input().split(" ")))
    lenList = len(listA)
    lenRod = int(input())
    twoDrray = [[0 for n in range(lenRod+1)] for k in range(lenList)]
    for k in range(lenList):
        for y in range(1,lenRod+1):
            if k  == 0:
                if y == listA[k]:
                    twoDrray[k][y] = 1
                elif y > listA[k] and twoDrray[k][y-listA[k]] > 0:
                    twoDrray[k][y] = twoDrray[k][y-listA[k]]+1
                else:
                    twoDrray[k][y] = 0
            else:
                if y == listA[k]:
                    twoDrray[k][y] = max(1,twoDrray[k-1][y])
                elif y > listA[k] and twoDrray[k-1][y-listA[k]] > 0:
                    twoDrray[k][y] = max(twoDrray[k-1][y-listA[k]]+1,twoDrray[k-1][y])
                else:
                    twoDrray[k][y] = twoDrray[k-1][y]
    print(twoDrray)
    print(twoDrray[lenList-1][lenRod])