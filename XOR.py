def maximizingXor(l, r):
    array = []
    for i in range(l,r+1):
        array.append(i)
    maxXor = 0
    for i in range(len(array)):
        for j in range(len(array)):
            calcXor = xor(array[i],array[j])
            if calcXor > maxXor:
                maxXor = calcXor
    return maxXor

def xor(a,b):
    return ((l | r) &  (~l | ~r))