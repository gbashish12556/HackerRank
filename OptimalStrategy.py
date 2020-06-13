testCases = int(input())

for n in range(testCases):

    array = list(map(int,input().split(" ")))
    lenArray = len(array)
    twoDArray = [[(0,0) for n in range(lenArray)] for k in range(lenArray)]

    for i in range(lenArray):
        twoDArray[i][i] = (array[i],0)
        if i < lenArray-1:
           twoDArray[i][i+1] = (max(array[i],array[i+1]),min(array[i],array[i+1]))


    for k in range(3,lenArray+1):
       for m in range(lenArray-k+1):
            if array[m]+twoDArray[m+1][m+k-1][1]  > array[m+k-1]+twoDArray[m][m+k-2][1]:
                twoDArray[m][m + k - 1] = (array[m]+twoDArray[m+1][m+k-1][1], twoDArray[m+1][m+k-1][0])
            else:
                twoDArray[m][m + k - 1] = (array[m+k-1]+twoDArray[m][m+k-2][1], twoDArray[m][m+k-2][0])

    print(twoDArray[0][lenArray-1][0])
