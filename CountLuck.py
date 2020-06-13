# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the countLuck function below.
def countLuck(matrix, k):
    rowMatrix = len(matrix)
    columnMatrix = len(matrix[0])
    startRow = 0
    startColumn = 0

    newMatrix = [['X' for u in range(columnMatrix + 2)] for v in range(rowMatrix + 2)]

    print(newMatrix)
    for y in range(1, rowMatrix + 1):
        for z in range(1,columnMatrix + 1):
            print(matrix[y - 1][z - 1])
            newMatrix[y][z] = matrix[y - 1][z - 1]
            if matrix[y - 1][z - 1] == "M":
                startRow = y
                startColumn = z
    print(newMatrix)
    totalCount = countTotal(newMatrix, startRow, startColumn)
    print(totalCount)
    if k == totalCount-10000:
        return "Impressed"
    else:
        return "Oops"


def countTotal(newMatrix, startRow, startColumn):
    if newMatrix[startRow][startColumn] == '*':
        return 10000
    ways = 0
    count = 0
    left = 0
    right = 0
    up = 0
    down = 0
    newMatrix[startRow][startColumn] = 'X'
    if newMatrix[startRow - 1][startColumn] == '.' or newMatrix[startRow - 1][startColumn] == '*':
        ways += 1
        up = countTotal(newMatrix, startRow - 1, startColumn)
    if newMatrix[startRow + 1][startColumn] == '.' or newMatrix[startRow + 1][startColumn] == '*':
        ways += 1
        down = countTotal(newMatrix, startRow + 1, startColumn)
    if newMatrix[startRow][startColumn - 1] == '.' or newMatrix[startRow][startColumn - 1] == '*':
        ways += 1
        left = countTotal(newMatrix, startRow, startColumn - 1)
    if newMatrix[startRow][startColumn + 1] == '.' or newMatrix[startRow][startColumn + 1] == '*':
        ways += 1
        right = countTotal(newMatrix, startRow, startColumn + 1)
    if ways > 1:
        # print("startRow"+str(startRow)+"startColumn"+str(startColumn))
        # print(newMatrix[startRow+1][startColumn])
        # print(newMatrix)
        count = 1 + max(left, right, up, down)
    else:
        count =  max(left, right, up, down)
    return count



t = int(input())

for t_itr in range(t):
    nm = input().split(" ")

    n = int(nm[0])

    m = int(nm[1])

    matrix = []

    for i in range(n):
        matrix_item = list(input())
        matrix.append(matrix_item)

    k = int(input())

    result = countLuck(matrix, k)

    print(result)