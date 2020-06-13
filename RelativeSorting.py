from collections import defaultdict

testCases = int(input())
for n in range(testCases):
    listA = list(map(int,input().split(" ")))
    setA = list(set(listA))
    lenSetA = len(setA)
    listB = list(map(int,input().split(" ")))
    lenA = len(listA)
    lenB = len(listB)
    count = {}
    for j in range(lenSetA):
        count[setA[j]] = 0

    # print(count)
    for l in range(lenA):
        # print(listA[l])
        count[listA[l]] += 1

    print(count)
    if lenB > 0:
        for k in range(lenB):
            # countB = count[listB[k]]
            if count[listB[k]] > 0:
                while count[listB[k]] > 0:
                    print(listB[k],end=' ')
                    count[listB[k]] -= 1

    for x in count.keys():
        # countA = count[x]
        if count[x] > 0:
            while count[x] > 0:
                print(x,end=' ')
                count[x] -= 1

