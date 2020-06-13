def lonelyInteger(array):
    array.sort()
    lenArray = len(array)
    for i in range(0,lenArray,2):
        if i < lenArray-1:
            if array[i] != array[i+1]:
                return array[i]
        else:
            return array[i]


testCases = int(input())
for n in range(testCases):
    array = list(map(int,input().split(" ")))
    print(lonelyInteger(array))