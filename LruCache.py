testCases = int(input())
for n in range(testCases):
    array = list(map(int, input().split(" ")))
    lruSize,lenArray = array[0],array[1]
    lru = list()
    array = list(map(int,input().split(" ")))
    for n in range(lenArray):
        if array[n] in lru:
            index = lru.index(array[n])
            print(index)
            lru = lru[:index]+lru[index+1:]
            lru.append(array[n])
        else:
            if len(lru) >= lruSize:
                lru = lru[1:lruSize]
            lru.append(array[n])