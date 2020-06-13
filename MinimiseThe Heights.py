testCases = int(input())
for n in range(testCases):
    valueK = int(input())
    lenArray = int(input())
    array = list(map(int,input().split(" ")))
    array.sort()
    # lenArray = len(array)
    small = array[0]+valueK
    big = array[lenArray-1]-valueK
    for j in range(1,lenArray-1):
        subtrack = array[j]-valueK
        add = array[j]+valueK
        if subtrack < small or add > big:
            if big - subtrack < add-small:
                small = subtrack
            else:
                big = add
    print(big-small)
