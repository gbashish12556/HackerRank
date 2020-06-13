
from collections import defaultdict
import copy

def buildingLights(edgemap,nodesNo,x,y):


    distanceMatix = [pow(10,10) for i in range(nodesNo)]

    bfsQue = list()
    bfsQue.append(x)
    distanceMatix[x-1] = 0

    while len(bfsQue) > 0:
        firstNode = bfsQue[0]
        bfsQue = bfsQue[1:]
        while len(edgemap[firstNode]) > 0 :
            edge = edgemap[firstNode].pop()
            node = edge[0]
            oldDistance = distanceMatix[node-1]
            newDistance = distanceMatix[firstNode-1]+edge[1]
            bfsQue.append(node)
            if newDistance < oldDistance:
                 distanceMatix[node-1] = newDistance

    if distanceMatix[y-1] < pow(10,10):
        return distanceMatix[y-1]
    else:
        return -1

road_nodes, road_edges = map(int, input().split())

road_from = [0] * road_edges
road_to = [0] * road_edges
road_weight = [0] * road_edges

for i in range(road_edges):
    road_from[i], road_to[i], road_weight[i] = map(int, input().split())

edgemap = defaultdict(list)

for i in range(road_edges):
    edgemap[road_from[i]].append([road_to[i],road_weight[i]])

q = int(input())

for q_itr in range(q):
    xy = input().split(" ")

    x = int(xy[0])

    y = int(xy[1])
    print(edgemap)
    print(buildingLights(copy.deepcopy(edgemap),road_nodes,x,y))
