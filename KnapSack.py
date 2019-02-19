def unboundedKnapsack(k, arr):

    count = [0]*(k+1)
    count[0] = 1
    for x in arr:
        for i in range(1,k+1):
            if i>=x:
                count[i] += count[i-x]
    for j in range(k,-1,-1):
        if count[j] >=1:
            return j

arr = "3 4 4 4 8"
arr = list(map(int, arr.split(" ")))
print(unboundedKnapsack(9, arr))