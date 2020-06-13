#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the larrysArray function below.
def larrysArray(A):
    lenArray = len(A)
    Acopy = A.copy()
    Acopy.sort()
    digDict = defaultdict(int)
    for i in range(lenArray):
        digDict[A[i]] = i

    for i in range(lenArray):
        value = i + 1

        while digDict[value] != i:

            index = digDict[value]

            # print("i: " +str(i)+"index: "+str(index)+"value: "+str(value)
            #       +"digDict: "+str(digDict))

            if index - i == 1 and index + 1 < lenArray:
                A1 = A[index - 1]
                B1 = value
                C1 = A[index + 1]

                A[index - 1] = B1
                A[index] = C1
                A[index + 1] = A1

                digDict[B1] = index - 1
                digDict[C1] = index
                digDict[A1] = index + 1

            elif index - i > 1 and index < lenArray:

                A1 = A[index - 2]
                B1 = A[index - 1]
                C1 = value

                A[index - 2] = C1
                A[index - 1] = A1
                A[index] = B1

                digDict[C1] = index - 2
                digDict[A1] = index - 1
                digDict[B1] = index

            else:
               return  "NO"

    if A == Acopy:
        return "YES"
    else:
        return "NO"



t = int(input())

for t_itr in range(t):
    n = int(input())

    A = list(map(int, input().rstrip().split()))

    result = larrysArray(A)

    print(result + '\n')

