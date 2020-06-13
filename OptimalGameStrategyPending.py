def calCMatrix(array,arraLen,F):
    for n in range(arraLen):
        for k in range(arraLen):
            if i == j:
                F[i][j] = array[i]
            if j == i+1:
                F[i][j] = max(arr[i],array[j])
            else:
                F[i][j] = max(array[i]+min(F[i+2][j],F[i+1][j-1]), arr[j]+min(F[i+1][j-1],F[i][j-2]))

testCases = int(input())
for n in range(testCases):
    arraLen = int(input())
    array = list(map(int,input().split(" ")))
    F = [[0 for n in range(arraLen)] for k in arraLen]
    calCMatrix(array,arraLen,F)
    value = F[0][arraLen-1]
    print(value)