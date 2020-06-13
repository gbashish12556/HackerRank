def calPalindrome(string):
    lenString = len(string)
    table = [[0 for x in range(lenString)] for y in range(lenString)]
    for x in range(lenString):
        table[x][x] = 1
    for x in range(lenString):
        for y in range(lenString):
            if x != y:
                if string[x] == string[y] and table[x+1][y-1] == 1:
                    table[x][y] = 1
                if string[x] == string[y] and y == x+1:
                    table[x][y] = 1
                else:
                    table[x][y] = 0
    print(table)


testCases = int(input())
for n in range(testCases):
    string = input()
    calPalindrome(string)