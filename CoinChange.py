def noOfWays(coinArray,arraySize,Cents):
    if Cents == 0:
        return 1
    if Cents < 0:
        return 0
    if Cents > 0 and arraySize <= 0:
        return 0
    return noOfWays(coinArray,arraySize,Cents-coinArray[arraySize-1])+noOfWays(coinArray,arraySize-1,Cents)


testCases = int(input())
for n in range(testCases):
    arraySize = int(input())
    coinArray = list(map(int,input().split(" ")))
    Cents = int(input())
    print(noOfWays(coinArray,arraySize,Cents))