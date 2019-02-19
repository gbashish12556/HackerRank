import os
import sys
from math import gcd

def getTotalX(a, b):

    lcm = a[0]
    for i in a[1:]:
        lcm = lcm*i//gcd(lcm, i)
    count = 0
    i = 1
    maxB =  min(b)
    while True:
        nextValue = lcm*i
        if  nextValue <= maxB :
            if all(x%nextValue == 0 for x in b):
                count +=1
        else:
            return count
        i +=1

a = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]
b= [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
print(getTotalX(a,b))
