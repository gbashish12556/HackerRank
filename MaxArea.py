def largestRectangle(h):
    position = []
    height = []
    maxArea = 0
    for i in range(len(h)):
        if len(position) == 0:
            position.append(i)
            height.append(h[i])
        elif h[i] > height[-1]:
            position.append(i)
            height.append(h[i])
        elif h[i] < height[-1]:
            while len(position) > 0 and h[i] < height[-1]:
                tempPos = position.pop()
                maxArea = max(maxArea, height.pop()*(i-tempPos))
            position.append(tempPos)
            height.append(h[i])
    while len(height) != 0:
        maxArea = max(maxArea, height.pop()*(i+1-position.pop()))
    return maxArea

arr = "8979 4570 6436 5083 7780 3269 5400 7579 2324 2116"
arr = list(map(int,arr.split(" ")))
print(largestRectangle(arr))