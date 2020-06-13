testCases = int(input())
for n in range(testCases):
    sumValue = int(input())
    array = list(set(list(map(int,input().split(" ")))))
    dict = {}
    lenArray = len(array)
    for n in range(lenArray-1):
        for k in range(n+1,lenArray):
            if n != k:
                sum = array[n]+array[k]
                dict[sum] = ((n),(k))
    for x in dict.keys():
        diff = sumValue - x
        # print(str(x)+" "+str(diff))
        if diff in dict:
            old_pair = tuple(dict[x])
            new_pair = tuple(dict[diff])
            if new_pair[0] != old_pair[0] and new_pair[0] != old_pair[1] and new_pair[1] != old_pair[0] and new_pair[1] != old_pair[1]:
                print(str(array[new_pair[0]])+" "+str(array[new_pair[1]])+" "+str(array[old_pair[0]])+" "+str(array[old_pair[1]]))
