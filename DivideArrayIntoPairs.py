testCases = int(input())
for n in range(testCases):
    k = int(input())
    array = list(map(int,input().split(" ")))
    dict = {}
    for x in array:
        remainder = x%k
        if remainder in dict.keys():
            dict[remainder] += 1
        else:
            dict[remainder] = 1
    status = "True"
    for x in dict.keys():
        half = k/2
        if x == 0 and dict[x]%2 != 0:
            status = "False"
        elif x == half and dict[x]%2 != 0:
            status = "False"
        elif k-x in dict.keys() and dict[x] != dict[k-x]:
            status = "False"
        elif k-x not in dict.keys():
            status = "False"
    print(status)

