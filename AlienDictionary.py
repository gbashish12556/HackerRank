from collections import defaultdict

def topoSort(graph):
    # Code here
    count = defaultdict(int)
    for (key, value) in graph.items():
        count[key] = 0
    for (key, value) in graph.items():
        for y in value:
            count[y] += 1
    # print(str(graph))
    # print(count)
    que = list()
    for k in count.keys():
        if count[k] == 0:
            que.append(k)
    newlist = list()
    while len(que)>0:
        node = que[0]
        newlist.append(node)
        if len(que) > 0:
            que = que[1:]
        for y in graph[node]:
            count[y] -= 1
            if count[y] == 0:
                que.append(y)
    return newlist

testCases = int(input())
for n in range(testCases):
    wordList = input().split(" ")
    lenWordList = len(wordList)
    graph = defaultdict(list)
    # count = defaultdict(int)
    for i in range(lenWordList-1):
        index = 0
        while index < len(wordList[i]) and index < len(wordList[i+1]):
            if wordList[i][index] != wordList[i+1][index]:
                # count[wordList[i+1][index]] += 1
                graph[wordList[i][index]].append(wordList[i+1][index])
                break
            index += 1
    print(topoSort(graph))
