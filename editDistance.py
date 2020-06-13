def editDistance(str1, str2, m, n):
    if n == 0:
        return m
    if m == 0:
        return 0
    if str1[0] == str2[0]:
        return editDistance(str1[1:],str2[1:], m-1, n - 1)
    else:
        return 1+min(editDistance(str1,str2[1:],m,n-1), editDistance(str1[1:],str2,m-1,n),editDistance(str1[1:],str2[1:], m-1, n - 1))

testCases = int(input())
for n in range(testCases):
    str1 = input()
    str2 = input()
    m = len(str1)
    n = len(str2)
    print(str(editDistance(str1,str2,m,n)))

