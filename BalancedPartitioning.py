

testCases = int(input())
for n in range(testCases):
    array = list(map(int,input().split(" ")))
    lenArray  = len(array)
    sumArray = sum(array)
    matrix = [[0 for i in range(sumArray+1)] for k in range(lenArray+1)]

    for l in range(lenArray+1):
        matrix[l][0] = 1

    for k in range(1,lenArray+1):
        for l in range(1,sumArray+1):
            # if k == 1 and l == 1:
            #     print(str(array[k]))
            if l-array[k-1]>=0:
                val = matrix[k-1][l-array[k-1]]
            else:
                val = 0
            matrix[k][l] = max(matrix[k-1][l],val)

    diff = 10000
    for k in range(int(sumArray/2),0,-1):
        if matrix[lenArray][k] == 1:
            diff = sumArray  - 2*k
            print(str(diff))
            break