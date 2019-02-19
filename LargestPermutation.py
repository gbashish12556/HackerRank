def largestPermutation(k, arr):

    lenArr = len(arr)
    index = [0]*(lenArr+1)
    for i in range(lenArr):
        index[arr[i]] = i
    for i in range(lenArr):
        if arr[i] != lenArr-i:
            index = index[lenArr-i]
            index[lenArr-i] = i
            index[arr[i]] = index
            arr[i], arr[index] = arr[index],arr[i]

            k -=1
        if k<=0:
            break
    return arr
