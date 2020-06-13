testCases = int(input())
for n in range(testCases):
    array = input().split(" ")
    lenArray = len(array)
    que = list()
    dict = {}
    for x in array:
        if x in dict.keys():
             if dict[x] == 1:
                 index = que.index(x)
                 que = que[:index]+que[index+1:]
             dict[x] = dict[x]+1
        else:
            que.append(x)
            dict[x] = 1
        if len(que) > 0:
            print(que[0],end=' ')
        else:
            print(-1,end=' ')

