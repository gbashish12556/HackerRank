def iWin(number):

    array = [2,3,5]

    if number == 0:
        return False

    if number < 0:
        return True

    for i in range(3):
        if iWin(number-array[i]) == False:
            return True
    return False



testCases = int(input())
for n in range(testCases):
    number = int(input())
    if iWin(number):
        print("First")
    else:
        print("Second")