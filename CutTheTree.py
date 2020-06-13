from collections import defaultdict

def cutTheTree(data, edges):

    NoOfNodes = len(data)
    NoOfEdges = len(edges)

    edgeMap = defaultdict(list)
    totalSum = sum(data)
    sumValue = [0 for i in range(NoOfNodes)]
    absDifference = pow(10,10)

    for j in range(NoOfEdges):
        edgeMap[edges[j][0]].append(edges[j][1])
        edgeMap[edges[j][1]].append(edges[j][0])

    waiting = [i+1 for i in range(1,NoOfNodes) if len(edgeMap[i+1]) == 1]

    while(len(waiting) > 0):

        print(waiting)
        for x in waiting:

            sumValue[x-1] += data[x-1]

            if len(edgeMap[x]) > 0:
                parentNode = edgeMap[x][0]
                edgeMap[parentNode].remove(x)
                sumValue[parentNode-1] += sumValue[x-1]

        waiting_new = list()

        for i in waiting:

            if len(edgeMap[i]) and len(edgeMap[edgeMap[i][0]]) == 1:
                waiting_new.append(edgeMap[i][0])

        waiting = list(set(waiting_new))

    for i in range(1,NoOfNodes):

        if abs(totalSum - 2*sumValue[i]) <  absDifference:
            absDifference = abs(totalSum - 2*sumValue[i])

    return absDifference


n = int(input().strip())

data = list(map(int, input().rstrip().split()))

edges = []

for _ in range(n - 1):
    edges.append(list(map(int, input().rstrip().split())))

result = cutTheTree(data, edges)

print(result)
