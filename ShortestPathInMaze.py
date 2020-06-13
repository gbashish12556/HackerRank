def shortestPath(x,y,m,n,array,visited):
    first,second,third,fourth = 1000,1000,1000,1000
    if x == m and y == n:
        return 0
    if(x-1 >= 0 and array[x-1][y] == 1 and visited[x-1][y] == 0):
        # print(str(x-1)+" : "+str(y))
        visited[x - 1][y] = 1
        first = shortestPath(x-1,y,m,n,array,visited)
    if(y-1 >= 0 and array[x][y-1] == 1 and visited[x][y-1] == 0):
        # print(str(x) + " : " + str(y-1))
        visited[x][y-1] = 1
        second = shortestPath(x,y-1,m,n,array,visited)
    if(x+1 < row and array[x+1][y] == 1 and visited[x+1][y] == 0):
        # print(str(x + 1) + " : " + str(y))
        visited[x+1][y] = 1
        third = shortestPath(x+1,y,m,n,array,visited)
    if(y+1 < column and array[x][y+1] == 1 and visited[x][y+1] == 0):
        # print(str(x) + " : " + str(y+1))
        visited[x][y+1] = 1
        fourth = shortestPath(x,y+1,m,n,array,visited)
    return 1+min(first,second,third,fourth)

testCases = int(input())
for n in range(testCases):
    array = list(map(int,input().split(" ")))
    row,column = array[0],array[1]
    arrayinput = list(map(int,input().split(" ")))
    array2 = list(map(int,input().split(" ")))
    destx,desty = array2[0],array2[1]
    # print("m: "+str(m)+" : n"+str(n))
    dArray = list()
    visited = [[0 for n in range(column)] for k in range(row)]
    for n in range(row):
        colArray = list()
        for k in range(column):
            # print(str(column)+" : "+str(n)+" : "+str(k))
            colArray.append(arrayinput[column*n+k])
        dArray.append(colArray)
    visited[0][0] = 1
    dist = shortestPath(0,0,destx,desty,dArray,visited)
    if(dist >= 1000):
        print("-1")
    else:
        print(str(dist))
