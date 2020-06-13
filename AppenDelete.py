def appendAndDelete(s, t, k):

    array1 = list(s)
    array2 = list(t)

    lenArray1 = len(array1)
    lenArray2 = len(array2)
    minLen = min(lenArray1,lenArray2)

    for i in range(minLen):
        if array1[i] != array2[i]:
            break
    if lenArray1+lenArray2 - 2*(i) <= k:
        return "Yes"
    else:
        return "No"

testCases = int(input())
for n in range(testCases):
     array = input().split(" ")
     print(appendAndDelete(array[0], array[1], int(array[2])))