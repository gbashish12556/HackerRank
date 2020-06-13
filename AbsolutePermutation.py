#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):

    mapped = list()
    setNew = set()
    for i in range(1,n+1):
        nos = list()
        no = (i+k)
        if no > 0 and  no <= n and no not in setNew:
            nos.append(i+k)
        no = (i-k)
        if no > 0 and  no <= n  and no not in setNew:
            nos.append(i-k)
        nos.sort()
        lenNos = len(nos)
        if len(nos) > 0:
             if k  <= n/2:
                setNew.add(nos[0])
                mapped.append(nos[0])
             else:
               setNew.add(nos[lenNos-1])
               mapped.append(nos[lenNos-1])
        else:
            return [-1]
    return mapped



t = int(input())

for t_itr in range(t):
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    result = absolutePermutation(n, k)

    print(' '.join(map(str, result)))
