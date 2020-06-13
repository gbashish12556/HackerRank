
from collections import defaultdict
import copy
def buildingLights(distanceMatrix,noOfNodes):
    for k in range(noOfNodes):
        oldCopy = copy.deepcopy(distanceMatix)
        for i in range(noOfNodes):
            for j in range(noOfNodes):
                    if k != i and k != j:
                        distanceMatrix[i][j] = min(oldCopy[i][j],oldCopy[i][k]+oldCopy[k][j])

    return distanceMatrix


road_nodes, road_edges = map(int, input().split())

road_from = [0] * road_edges
road_to = [0] * road_edges
road_weight = [0] * road_edges

for i in range(road_edges):
    road_from[i], road_to[i], road_weight[i] = map(int, input().split())

q = int(input())

edgeNew = defaultdict(list)

for k in range(road_edges):
        edgeNew[road_from[k]].append([road_to[k],road_weight[k]])

distanceMatix = []

for i in range(road_nodes):
    newArra = list()
    distanceMatix.append((newArra))
    for j in range(road_nodes):
        if i == j:
            val = 0
        else:
            val = pow(10, 10)
        newArra.append(val)

for k in range(road_edges):
    distanceMatix[road_from[k]-1][road_to[k]-1] = road_weight[k]


distanceMatix = buildingLights(distanceMatix,road_nodes)

for q_itr in range(q):
    xy = input().split()

    x = int(xy[0])

    y = int(xy[1])
    if distanceMatix[x-1][y-1] < pow(10,10):
         print(distanceMatix[x-1][y-1])
    else:
        print(-1)
