#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    matrixRow = len(matrix)
    matrixColumn = len(matrix[0])
    rowLayer = int(min(matrixRow,matrixColumn) / 2)

    for i in range(rowLayer):

        circleRound = 2*(matrixRow-1-2*i)+2*(matrixColumn-2*i-1)
        remain = r%circleRound
        for x in range(remain):


            #Go left
            temp1 = matrix[i][i]
            for k in range(i+1,matrixColumn-i):
                matrix[i][k-1] = matrix[i][k]

            #Go Down
            temp2 = matrix[matrixRow-1-i][i]
            for l in range(matrixRow-2-i,i-1,-1):
                if l == i:
                    matrix[l + 1][i] = temp1
                else:
                    matrix[l + 1][i] = matrix[l][i]

            #Go Right
            temp1 = matrix[matrixRow-1-i][matrixColumn-1-i]

            for m in range(matrixColumn-2-i,i-1,-1):
                if m == i:
                    matrix[matrixRow-1-i][m+1] = temp2
                else:
                    matrix[matrixRow-1-i][m+1] = matrix[matrixRow-1-i][m]

            #Go up
            for k in range(i+1,matrixRow-i):
                if k == matrixRow-i-1:
                    matrix[k-1][matrixColumn-1-i] = temp1
                else:
                    matrix[k-1][matrixColumn-1-i] = matrix[k][matrixColumn-1-i]
    return matrix


mnr = input().rstrip().split()

m = int(mnr[0])

n = int(mnr[1])

r = int(mnr[2])

matrix = []

for _ in range(m):
    matrix.append(list(map(int, input().rstrip().split())))

print(matrixRotation(matrix, r))
