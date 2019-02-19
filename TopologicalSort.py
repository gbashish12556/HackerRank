from collections import defaultdict
def topoSort(n, graph):
    stack = list()
    visited = [False]*50
    for i in range(n):
        if graph[i] is not None:
            if visited[i]  == False:
                visited[i] = True
                dfs(n, graph, stack,i,visited)
    stack = rEverse(stack)
    return stack


def rEverse(stack):
    n = len(stack)
    for i in range(n//2):
        stack[i], stack[n-1-i] = stack[n-1-i], stack[i]
    return stack
def dfs(n, graph, stack, x, visited):

    for j in range(len(graph[x])):
        if visited[graph[x][j]] == False:
            visited[graph[x][j]] = True
            dfs(n, graph, stack, graph[x][j], visited)

    stack.append(x)

def creategraph(e, n, arr, graph):
    i = 0
    while i<2*e:
        graph[arr[i]].append(arr[i+1])
        i+=2

t = int(input())
for i in range(t):
    e,N = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    graph = defaultdict(list)
    creategraph(e, N, arr, graph)
    res = topoSort(N, graph)
    valid=True
    for i in range(N):
        n = len(graph[res[i]])
        for j in range(len(graph[res[i]])):
            for k in range(i+1, N):
                # print("ashish")
                # print(k)
                # print(i)
                # print(j)
                if res[k]==graph[res[i]][j]:
                    n-=1
        # print n
        if n!=0:
            valid=False
            break
    if valid:
        print(1)
    else:
        print(0)

