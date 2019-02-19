def candies(arr):
    totalCandy = 1
    lenArr = len(arr)
    candidatesCandy = [0]*lenArr
    candidatesCandy[0] = 1
    for i in range(1,lenArr):
        if arr[i] < arr[i-1]:
            if candidatesCandy[i-1] == 1:
                candidatesCandy[i - 1] = 2
                totalCandy +=1
                j = i-1
                while j>=1 and arr[j] < arr[j-1]:
                    if candidatesCandy[j - 1] == candidatesCandy[j]:
                        candidatesCandy[j - 1] = candidatesCandy[j - 1]+1
                        j -=1
                        totalCandy += 1
                    else:
                        break
            candidatesCandy[i] = 1
        elif arr[i] > arr[i-1]:
            candidatesCandy[i] = candidatesCandy[i-1]+1
        else:
            candidatesCandy[i] = 1
        totalCandy += candidatesCandy[i]
    return totalCandy

arr = [2,4,2,6,1,7,8,9,10,2,3,4,3,2,1,2,3,4]
print(candies(arr))