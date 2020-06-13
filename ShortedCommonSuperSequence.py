def shortestLCS(str1,str2,str1Len,str2Len):
    lcs =  [[0 for n in range(str1Len+1)] for y in range(str2Len+1)]
    for i in range(str2Len):
        for j in range(str1Len):
            if str2[i] == str1[j]:
                lcs[i+1][j+1] = lcs[i][j])+1
            else:
                lcs[i + 1][j + 1] = max(lcs[i][j+1],lcs[i+1][j])
    return lcs[str2Len][str1Len]


testCases = int(input())
for n in range(testCases):
    string = input().split(" ")
    str1,str2 = string[0],string[1]
    str1Len = len(str1)
    str2Len = len(str2)
    # shortestLCS(str1, str2, str1Len, str2Len),
    print(str1Len+str2Len-shortestLCS(str1, str2, str1Len, str2Len))