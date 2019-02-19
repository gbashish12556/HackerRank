# 1
# 8
# 0 44 20 14 21 37 46 44 44 0 35 27 47 6 33 1 20 35 0 42 32 47 46 38 14 27 42 0 6 30 15 9 21 47 32 6 0 14 18 27 37 6 47 30 14 0 35 29 46 33 46 15 18 35 0 39 44 1 38 9 27 29 39 0
# 0

def dijkstra(graph, v, s):

    # Code here
    que = list()
    que.append(s)
    distance = [1000 * v] * v
    distance[s] = 0
    visited = [False] * v
    calculateDistance(que, distance, visited, graph, v)
    que.append(s);
    visited[s] = True
    for i in range(len(distance)):
        print(distance[i], end=' ')


def calculateDistance(que, distance, visited, graph, v):

    while len(que) > 0:
        last = que.pop(0)
        for i in range(v):
            if visited[i] == False:
                visited[i] = True
                que.append(i)
            if graph[last][i] + distance[last] < distance[i]:
                distance[i] = graph[last][i] + distance[last]


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    matrix = [[0 for i in range(n)] for j in range(n)]
    c = 0
    # print(arr)
    for i in range(n):
        for j in range(n):
           matrix[i][j] = arr[c]
           c += 1
    s = int(input())
    dijkstra(matrix, n, s)
