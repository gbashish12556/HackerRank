#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the almostSorted function below.
def almostSorted(arr):

    arrayCopy = arr.copy()
    arrayCopy.sort()
    lenArray = len(arr)

    diffFirstIndex= -1
    diffLastIndex = 0

    for i in range(lenArray):
        print(str(i)+" : "+str(arr[i])+" : "+str(arrayCopy[i]))
        if arr[i] != arrayCopy[i]:
            if diffFirstIndex == -1:
                diffFirstIndex = i
            diffLastIndex = i
    temp = arr[diffFirstIndex]
    arr[diffFirstIndex] = arr[diffLastIndex]
    arr[diffLastIndex] = temp
    if arr != arrayCopy:
        temp = arr[diffFirstIndex]
        arr[diffFirstIndex] = arr[diffLastIndex]
        arr[diffLastIndex] = temp
        arr[diffFirstIndex:diffLastIndex + 1] =reversed(arr[diffFirstIndex:diffLastIndex + 1])
        if arr == arrayCopy:
            print("yes")
            print("reverse " + str(i+1) + " " + str(diffLastIndex+1))
            return
    else:
        print("yes")
        print("swap " + str(i+1) + " " + str(diffLastIndex+1))
        return

    print("no")


n = int(input())

arr = list(map(int, input().rstrip().split()))

almostSorted(arr)
