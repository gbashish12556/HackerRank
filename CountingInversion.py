def findInversionCount(array, arrayLen):
    arrayCopy = array.copy()
    arrayCopy.sort(key=int)
    count = 0
    for n in range(arrayLen):
        if array[n] != arrayCopy[n]:
            temp = array[n]
            array[n] = arrayCopy[n]
            array[arrayCopy.index(temp)] = temp
            count = count+1
    return count

testCases = int(input())
for n in range(testCases):
    lenArray = int(input())
    array = list(map(int,input().split(" ")))
    found = findInversionCount(array,lenArray)
    print(found)