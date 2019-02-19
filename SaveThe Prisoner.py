def saveThePrisoner(n, m, s):
    return m%n+s-1


arr = "46934 543563655 46743"
arr = list(map(int, arr.split(" ")))
n= arr[0]
m = arr[1]
s = arr[2]
print(saveThePrisoner(n, m, s))

[1,0,1,0,1,1,0,0,0,1,1]
