# code

# 1
# 3 15
# 1 1 1 0 0 0 0 1 1 1 1 1 0 1 1 1 1 1 1 0 0 0 0 1 1 0 0 0 1 1 0 0 0 0 0 1 0 0 0 1 1 1 0 0 0
# 2 3

# 1
# 3 15
# 1 1 1 0 0 0 0 1 1 1 1 1 0 1 1
# 1 1 1 1 0 0 0 0 1 1 0 0 0 1 1
# 0 0 0 0 0 1 0 0 0 1 1 1 0 0 0
# 2 3

# code
def Components(matrix, visited, x, y, n, m, distance):

    if isSafe(x - 1, y, n, m, matrix):
        if visited[x - 1][y] == False:
            visited[x - 1][y] = True
            distance[x - 1][y] = min(distance[x - 1][y], distance[x][y] + 1)
            Components(matrix, visited, x - 1, y, n, m, distance)
        else:
            distance[x - 1][y] = min(distance[x - 1][y], distance[x][y] + 1)
    if isSafe(x + 1, y, n, m, matrix):
        if visited[x + 1][y] == False:
            visited[x + 1][y] = True
            distance[x + 1][y] = min(distance[x + 1][y], distance[x][y] + 1)
            Components(matrix, visited, x + 1, y, n, m, distance)
        else:
            distance[x + 1][y] = min(distance[x + 1][y], distance[x][y] + 1)
    if isSafe(x, y - 1, n, m, matrix):
        if visited[x][y - 1] == False:
            visited[x][y - 1] = True
            distance[x][y - 1] = min(distance[x][y - 1], distance[x][y] + 1)
            Components(matrix, visited, x, y - 1, n, m, distance)
        else:
            distance[x][y - 1] = min(distance[x][y - 1], distance[x][y] + 1)
    if isSafe(x, y + 1, n, m, matrix):
        if visited[x][y + 1] == False:
            visited[x][y + 1] = True
            distance[x][y + 1] = min(distance[x][y + 1], distance[x][y] + 1)
            Components(matrix, visited, x, y + 1, n, m, distance)
        else:
            distance[x][y + 1] = min(distance[x][y + 1], distance[x][y] + 1)


def isSafe(x, y, n, m, matrix):
    if x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1 and matrix[x][y] == 1:
        return True
    return False


t = int(input())
while t > 0:
    n, m = list(map(int, input().split(" ")))
    arrInput = list(map(int, input().split(" ")))
    x, y = list(map(int, input().split(" ")))
    c = 0
    maxCount = n + m
    count = 0
    matrix = list()
    visited = [[False for i in range(m)] for j in range(n)]
    distance = [[n * m for i in range(m)] for j in range(n)]
    distance[x][y] = 0
    for i in range(n):
        matrix.append(list())
        for j in range(m):
            matrix[i].append(arrInput[c])
            c += 1
    Components(matrix, visited, x, y, n, m, distance)
    if distance[0][0] == n*m:
        print(-1)
    else:
        print(distance[0][0])
    t -= 1
