def substringDiff(k, s1, s2):

    lenS = len(s1)
    maxLen = 0

    for i in range(lenS):
        for j in range(lenS):

            if s1[i] == s2[j]:
                diff = 0
                i1 = i
                j1 = j
                while i1 <lenS-1 and j1 <lenS-1 and diff<=k:
                    i1 += 1
                    j1 += 1
                    if s1[i1] != s2[j1]:
                        diff +=1
                i2 = i
                j2 = j
                if i==0 and j ==3:
                    print(diff)
                    print(str(i) + " : " + str(j))
                while i2 >0 and j2 >0 and diff <= k:
                    i2 -= 1
                    j2 -= 1
                    if s1[i2] != s2[j2]:
                        diff +=1
                if i == 0 and j == 3:
                    print(diff)
                    print(str(i1)+" : "+str(i2))
                if diff > k:
                    newDiff = i1 - i2
                else:
                    newDiff = i1 - i2 + 1
                if maxLen < newDiff:
                    maxLen  = newDiff
    return maxLen

k = 0
s1 = "abacba"
s2 = "abcaba"
print(substringDiff(k, s1, s2))