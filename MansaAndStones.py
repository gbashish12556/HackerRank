def stones(n, a, b):
    valArr = [a,b]
    maxVal = max(valArr)*(n-1)
    result = []
    # print(valCount)
    for x in valArr:
        valCount = [[0] for i in range(maxVal + 1)]
        for i in range(maxVal+1):
            if i >= x:
                valCount[i] = valCount[i-x].copy()
                valCount[i].append(x)
                if len(valCount[i]) == n:
                    result.append(i)
                print(valCount)

    return result

print(stones(3,1,2))