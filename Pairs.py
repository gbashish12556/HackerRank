def pairs(k, arr):
    arr.sort(key =int)
    lenArr = len(arr)
    currentIndex = 0
    firstIndex = 0
    counts = [0]*lenArr
    for i in range(1,lenArr):
        for j in range(currentIndex,i):
            diff = arr[i]-arr[j]
            if diff == k:
                if counts[i] == 0:
                    firstIndex = j
                counts[i] +=1
            elif diff < k:
                currentIndex = firstIndex
                break
    return sum(counts)

arr = "1 3 5 8 6 4 2"
arr = list(map(int,arr.split(" ")))
print(pairs(2, arr))