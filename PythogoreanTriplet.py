def printPythagorean(array, lenArray):
    for n in range(lenArray):
        array[n] = pow(array[n],2)
    array.sort(key = int)
    maxIndex = lenArray
    while maxIndex >  2:
        maxIndex = maxIndex-1
        highIndex = maxIndex - 1
        lowIndex = 0
        while lowIndex < highIndex:
            maxVal = array[maxIndex]
            highVal = array[highIndex]
            lowVal = array[lowIndex]
            sum = lowVal + highVal
            if sum > maxVal:
                highIndex = highIndex-1
            elif sum < maxVal:
                lowIndex = lowIndex+1
            elif sum == maxVal:
                return "Yes"
    return "No"


testCases = int(input())
for n in range(testCases):
    lenArray = int(input())
    array = list(map(int,input().split(" ")))
    found = printPythagorean(array,lenArray)
    print(found)