testCases = int(input())
for n in range(testCases):
    lenArray = int(input())
    array = list(map(int,input().split(" ")))
    stack = list()
    stack.append(array[0])
    for n in range(1,lenArray):
        if array[n] > array[n-1]:
            while len(stack) > 0:
                stack.pop()
                print(array[n], end=' ')
            stack.append(array[n])
        else:
            stack.append(array[n])
    while len(stack) > 0:
        stack.pop()
        print(-1, end=' ')