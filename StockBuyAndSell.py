def profitDays(array,lenArray):
    buyDay  = -1
    for n in range(lenArray-1):
        if array[n] < array[n+1] and array[buyDay]  > array[n]:
            buyDay = n
        elif array[n] > array[n+1] and n != 0:
            sellDay = n
            print("("+str(buyDay)+" "+str(sellDay)+")", end=" ")
            buyDay = n + 1
    if n == lenArray-2 and buyDay != -1:
        sellDay = lenArray-1
        print("(" + str(buyDay) + " " + str(sellDay) + ")", end="")


testCases = int(input())
for n in range(testCases):
    lenArray = int(input())
    array = list(map(int,input().split(" ")))
    profitDays(array,lenArray)
