
# from collections import list

testCases = int(input())
for n in range(testCases):
    noOfBoxes = int(input())
    totalBoxMatrix = list()
    for n in range(noOfBoxes):
        WHL = list(map(int,input().split(" ")))
        totalBoxMatrix.append([WHL[0] * WHL[1], WHL[0], WHL[1], WHL[2]])
        totalBoxMatrix.append([WHL[1] * WHL[2], WHL[1], WHL[2], WHL[0]])
        totalBoxMatrix.append([WHL[2] * WHL[0], WHL[2], WHL[0], WHL[1]])
    totalBoxMatrix = sorted(totalBoxMatrix, key=lambda l:l[0],reverse=True)
    lenTotalBox = len(totalBoxMatrix)
    maxHeights = list()

    for k in range(lenTotalBox):
        maxHeights.append(totalBoxMatrix[k][3])

    for i in range(1,lenTotalBox):
        for j in range(0,i):
            # if i  == 4 and j == 0:
                if totalBoxMatrix[i][1] < totalBoxMatrix[j][1] and totalBoxMatrix[i][2] < totalBoxMatrix[j][2]  or totalBoxMatrix[i][1] < totalBoxMatrix[j][2] and totalBoxMatrix[i][2] < totalBoxMatrix[j][1]:

                   maxHeights[i] = max(totalBoxMatrix[i][3]+maxHeights[j],maxHeights[i])

    print(max(maxHeights))