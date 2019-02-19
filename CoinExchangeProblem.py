def getWays(n, c):
    ways = [0]*(n+1)
    ways[0] =1
    for x in c:
        for i in range(n+1):
            if i >= x:
                ways[i] += ways[i-x]
    print(ways[n])

c = [1, 2, 3]
getWays(4,c)