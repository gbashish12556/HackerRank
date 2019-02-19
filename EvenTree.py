
def evenForest(t_nodes, t_edges, t_from, t_to):
    global nodesChild
    nodesChild = [1]*t_nodes
    global visitedNodes
    visitedNodes = [0] * t_nodes
    global neighbours
    neighbours = [[] for j in range(t_nodes)]

    for i in range(t_edges):
        neighbours[t_from[i]-1].append(t_to[i]-1)
        neighbours[t_to[i]-1].append(t_from[i]-1)
    visitedNodes[0] = 1
    countNode(0)
    count = 0
    for x in range(1,t_nodes):
        if nodesChild[x] % 2 == 0:
            count +=1
    return count

def countNode(node):
    for x in neighbours[node]:
        if visitedNodes[x] == 0:
            visitedNodes[x] = 1
            nodesChild[node] += countNode(x)
    return nodesChild[node]

t_nodes = 10
t_edges = 9
t_from = [2,3,4,5,6,7,8,9,10]
t_to =   [1,1,3,2,1,2,6,8,8]
print(evenForest(t_nodes, t_edges, t_from, t_to))