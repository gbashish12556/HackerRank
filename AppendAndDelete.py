def appendAndDelete(s, t, k):
    count = 0
    if len(s) >len(t):
        count +=len(s)-len(t)
    if len(s) < len(t):
        count += len(t)-len(s)
    for i in range(min(len(s),len(t))):
        if s[i] != t[i]:
            count += (min(len(s),len(t))-i)*2
            break

    if count <= k:
        return "Yes"
    else:
        return "No"
s = "y"
t = "yu"
k =2
print(appendAndDelete(s, t, k))
