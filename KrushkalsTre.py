def kruskals(g_nodes, g_from, g_to, g_weight):
    weightArray = []
    lenEdges = len(g_weight)
    for i in range(lenEdges):
        weightArray.append([g_from[i],g_to[i],g_weight[i]])
    weightArray = sorted(weightArray, key=lambda x:x[2])
    arr = []
    sumTotal = 0
    countEdges = 0
    for i in range(lenEdges):
        arr.append(weightArray[i][0])
        arr.append(weightArray[i][1])
        if isCycle(arr):
            arr.pop()
            arr.pop()
        else:
            sumTotal += weightArray[i][2]
            countEdges +=1
            if countEdges == g_nodes-1:
                return sumTotal


def isCycle(arr):

    lenArr = len(arr)
    setArr = set(arr)
    lenSet = len(setArr)
    if lenArr > (lenSet-1)*2:
        return True
    else:
        return False

g_nodes =5
g_from = [3,5,4,3,1]
g_to = [5,4,3,1,2]
g_weight = [1,2,3,4,5]
print(kruskals(g_nodes, g_from, g_to, g_weight))