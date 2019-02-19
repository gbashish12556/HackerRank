def legoBlocks(totalHeight, totalWidth):
    ways = [[0 for i in range(totalWidth+1)] for j in range(totalHeight)]
    print(ways)
    ways[0] = 1
    newBreakPoint = set()
    widths = [1,2,3,4]
    ways = [[0] for j in range(totalHeight)]
    newBreakPoint = set()
    for k in range(len(widths)):
        print(newBreakPoint)
        breakPoints = newBreakPoint
        newBreakPoint = set()
        for i in range(totalHeight):
            ways[i][0] = ways[i-1][totalWidth]
            for j in range(totalWidth):
                if j >= widths[k] and breakPoints.count(j) == 0:
                    ways[i][j] += ways[i][widths[k] - i]
                    if ways[i][j] != 0:
                        newBreakPoint.add(j)
    return ways[totalHeight-1][totalWidth]



totalHeight = 2
totalWidth = 2
print(legoBlocks(totalHeight, totalWidth))