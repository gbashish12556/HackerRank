testCases = int(input())
for n in range(testCases):
    string1 = input()
    lenString = len(string1)
    twoDArray  = [[0 for n in range(lenString)] for k in range(lenString)]
    for i in range(lenString):
        twoDArray[i][i] = 1
        if i < lenString-1 and string1[i] == string1[i+1]:
            twoDArray[i][i+1] = 1
    # print(twoDArray)
    start = 0
    end = 0
    maxLen = 0
    for len in range(3,lenString+1):
        for j in range(0,lenString-len+1):
            # if(len == 6 and j == 2):
            #     print(str(string1[j]) + " : " + str(string1[j + len - 1]))
            #     print(str(j) + " : " + str(j + len - 1)+" : "+str(twoDArray[j+1][j+len-2]))
                if string1[j] == string1[j+len-1] and twoDArray[j+1][j+len-2] == 1:
                    twoDArray[j][j+len-1] = 1
                    # print(twoDArray)
                    if(len > maxLen):
                        start = j
                        end = j+len-1
                        maxLen = len
                        # print(str(maxLen) + " : " + str(i) + " : " + str(j))
    print("Start: "+str(start)+" End: "+str(end)+" maxLen: "+str(maxLen))
