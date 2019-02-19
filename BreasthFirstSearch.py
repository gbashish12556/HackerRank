def bfs(n, m, edges, s):
    distances = [-1]*n
    stack = [s]
    distances[s-1] = 0
    neighbours = [[] for i in range(n)]
    for j in range(m):
        neighbours[edges[j][0]-1].append(edges[j][1])
        neighbours[edges[j][1]-1].append(edges[j][0])

    while len(stack) > 0:
        last = stack.pop(0)
        for x in neighbours[last-1]:
                if distances[x-1] == -1:
                     distances[x-1] = distances[last-1]+6
                     stack.append(x)
    return distances[0:s-1]+distances[s:]

n=10
m =4
edges = [[3,1],[10,1],[1,8],[5,2]]
s = 3
print(bfs(n, m, edges, s))
