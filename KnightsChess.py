import copy

def printShortestPath(n, i_start, j_start, i_end, j_end):

    visitedMatrixLen = n+2*(n-1)
    visitedMatrix = [[[-1,list()] for i in range(visitedMatrixLen)] for j in range(visitedMatrixLen)]
    nodeQue = list()
    nodeQue.append([n-1+i_start, n-1+j_start])
    for k in range(0,n):
        for l in range(0,n):
            visitedMatrix[k+n-1][l+n-1] = [100000,list()]
    visitedMatrix[n-1+i_start][n-1+j_start] = [0,list()]

    newMatrix = copy.deepcopy(visitedMatrix)
    visitedMatrixFinal  = BFS(newMatrix, nodeQue,n,i_end,j_end)
    endNodeValue = visitedMatrixFinal[n - 1+i_end][n - 1+j_end]
    if endNodeValue[0] < 100000:
      print(len(endNodeValue[1]))
      print(" ".join(endNodeValue[1]))
    else:
      print("Impossible")


def BFS(vistedMatrix, nodeQue,n,i_end,j_end):

    steps = {"UR":[-2,1],"R":[0,2],"LR":[2,1],"LL":[2,-1],"UL":[-2,-1],"L":[0,-2]}

    curentRowPosition = nodeQue[0][0]
    currentColumnPosition = nodeQue[0][1]
    if curentRowPosition == n - 1+i_end and currentColumnPosition == n - 1+j_end:
        return vistedMatrix
    nodeQue = nodeQue[1:]

    for x in steps:

        currentValue = vistedMatrix[curentRowPosition][currentColumnPosition][0]

        currentList = vistedMatrix[curentRowPosition][currentColumnPosition][1]
        rowStep = steps[x][0]
        columStep = steps[x][1]
        nextRow = curentRowPosition+rowStep
        nextColumn = currentColumnPosition+columStep
        i_end_new = i_end+n-1
        j_end_new = j_end+n-1

        if (nextRow >= curentRowPosition and nextColumn >= currentColumnPosition and i_end_new >= curentRowPosition and j_end_new >= currentColumnPosition) or (nextRow <= curentRowPosition and nextColumn >= currentColumnPosition and i_end_new <= curentRowPosition and j_end_new >=currentColumnPosition) or (nextRow >= curentRowPosition and nextColumn <= currentColumnPosition and i_end_new >= curentRowPosition and j_end_new  <= currentColumnPosition) or (nextRow <= curentRowPosition and nextColumn <= currentColumnPosition and i_end_new <= curentRowPosition and j_end_new <= currentColumnPosition):


            if currentValue + 1 < vistedMatrix[curentRowPosition + steps[x][0]][

                currentColumnPosition + steps[x][1]][0]:

                nextList = currentList.copy()
                nextList.append(x)

                vistedMatrix[nextRow][nextColumn] = [currentValue +1, nextList]

                nodeQue.append([nextRow, nextColumn])


    if (len(nodeQue) > 0):
        return BFS(vistedMatrix, nodeQue,n,i_end,j_end)
    else:
        return vistedMatrix




n = int(input())
array = list(map(int,input().split(" ")))
i_start = array[0]
j_start = array[1]
i_end = array[2]
j_end = array[3]
printShortestPath(n,i_start,j_start,i_end,j_end)