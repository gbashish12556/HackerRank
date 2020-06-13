#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#



def kruskals(g_nodes, g_from, g_to, g_weight):

    parent = [-1 for i in range(g_nodes)]
    nofOfEdgges = len(g_from)
    nodesList = list()
    total = 0

    for i in range(nofOfEdgges):
        fromNode = g_from[i]
        toNode = g_to[i]
        nodesList.append([fromNode, toNode, g_weight[i]])
    nodesList = sorted(nodesList, key=lambda x: x[0])
    nodesList = sorted(nodesList, key=lambda x: x[1])
    nodesList = sorted(nodesList, key=lambda x: x[2])

    for i in range(nofOfEdgges):

        startNode = nodesList[i][0]-1
        endNode =  nodesList[i][1] - 1
        if findParent(parent,startNode) != findParent(parent,endNode):
            total += nodesList[i][2]
            makeUnion(parent,startNode,endNode)

    return total

def findParent(parent,x):
    if parent[x] == -1:
        return x
    else:
        return findParent(parent,parent[x])

def makeUnion(parent,x,y):
    x_parent = findParent(parent,x)
    y_parent = findParent(parent,y)
    parent[x_parent] = y_parent

g_nodes, g_edges = map(int, input().rstrip().split())

g_from = [0] * g_edges
g_to = [0] * g_edges
g_weight = [0] * g_edges

for i in range(g_edges):
    g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

res = kruskals(g_nodes, g_from, g_to, g_weight)

print(res)
