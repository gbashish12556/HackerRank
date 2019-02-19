def jumpingOnClouds(c):
    count = 0
    currentPosition = 0
    lastPosition = len(c) - 1
    while currentPosition < lastPosition:

        if currentPosition - lastPosition >= 2 and c[currentPosition + 2] == 0 and currentPosition + 2 <= lastPosition:
            count += 1
            currentPosition = currentPosition + 2
        else:
            count += 1
            currentPosition = currentPosition + 1
        print(currentPosition)
    return count

arr = "0 0 1 0 0 1 0"
arr = arr.split(" ")
print(jumpingOnClouds(arr))