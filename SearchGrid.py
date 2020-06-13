#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gridSearch function below.
def gridSearch(G, P):
    rowGrid = len(G)
    columnGrid = len(G[0])
    rowPattern = len(P)
    columnPattern = len(P[0])
    for i in range(rowGrid):
        for j in range(columnGrid):
            if G[i][j] == P[0][0] and (rowGrid - i) >= rowPattern and (columnGrid - j) >= columnPattern:
                status = 0
                for k in range(rowPattern):
                    for l in range(columnPattern):
                        if P[k][l] != G[i + k][j + l]:
                            status = 1
                            break
                    if status == 1:
                        break
                if status == 0:
                    return "Yes"
    return "No"



t = int(input())

for t_itr in range(t):
    RC = input().split()

    R = int(RC[0])

    C = int(RC[1])

    G = []

    for _ in range(R):
        G_item = input()
        G.append(G_item)

    rc = input().split()

    r = int(rc[0])

    c = int(rc[1])

    P = []

    for _ in range(r):
        P_item = input()
        P.append(P_item)

    result = gridSearch(G, P)

    print(result)