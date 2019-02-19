def quickestWayUp(ladders, snakes):

    visitStack = [[1,0]]
    visitedNodes = [0]*101
    visitedNodes[0] = 1
    visitedNodes[1] = 1
    laddersDict = {}
    snakesDict = {}
    for i in range(len(ladders)):
        laddersDict[ladders[i][0]] = ladders[i][1]
    for i in range(len(snakes)):
        snakesDict[snakes[i][0]] = snakes[i][1]

    while (len(visitStack)>0):
        lastVisited = visitStack.pop(0)

        lastVisitedPosition = lastVisited[0]
        lastVisitedCount =  lastVisited[1]
        i = 6
        while(i>0):
            nextPosition = lastVisitedPosition+i
            if nextPosition <= 100:
                if nextPosition in laddersDict:
                    nextPosition = laddersDict[nextPosition]
                elif nextPosition in snakesDict:
                    nextPosition = snakesDict[nextPosition]
                if visitedNodes[nextPosition] == 0:
                    visitedNodes[nextPosition] = 1
                    visitStack.append([nextPosition,lastVisitedCount+1])
                    print(visitStack)
                    if nextPosition == 100:
                        return lastVisitedCount+1
            i -= 1

ladders = [[32,62],[42,68],[12,98]]
snakes = [[95, 13],[97, 25],[93, 37],[79, 27],[75, 19],[49, 47],[67, 17]]
quickestWayUp(ladders, snakes)