def highestValuePalindrome(s, n, k):

    totalMisMatch = 0
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            totalMisMatch +=1
    if k < totalMisMatch:
        return -1
    if len(s) == 1 and k > 0:
        return str(9)

    for j in range(n//2):
        if s[j] == s[n-1-j] and s[j] != '9' and k-2>=totalMisMatch:
            s = s[:j] + str(9) + s[j + 1:n - 1 - j] + str(9) + s[n - j:]
            k -= 2
        elif s[j] != s[n-1-j]:
            if s[j] != '9' and s[n-1-j] != '9' and k-2 >= totalMisMatch-1:
                s = s[:j] + str(9) + s[j + 1:n - 1 - j] + str(9) + s[n - j:]
                k -= 2
            elif s[j] != '9' and s[n-1-j] == '9' and k-1 >= totalMisMatch-1 :
                s = s[:j] + str(9) + s[j + 1:]
                k -= 1
            elif s[j] == '9' and s[n-1-j] == '9' and k-1 >= totalMisMatch-1 :
                s = s[:n - 1 - j] + str(9) + s[n - j:]
                k -= 1
            else:
                if int(s[j]) > int(s[n-1-j]):
                    s = s[:n - 1 - j] + s[j] + s[n - j:]
                else:
                    s = s[:j] + s[n-1-j] + s[j + 1:]
                k -= 1
            totalMisMatch -= 1

    return s

s = "092282"
print(highestValuePalindrome(s, 6, 3))