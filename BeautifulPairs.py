def beautifulTriplets(d, arr):
    pairs = []
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i] - arr[j] == d:
               pairs.append([j,i])
    count = 0

    for i in range(1,len(pairs)):
        for j in range(i):
            if pairs[i][0] == pairs[j][1]:
                count +=1
    return count

arr  = "1 2 4 5 7 8 10"
arr = list(map(int,arr.split(" ")))
print(beautifulTriplets(3, arr))