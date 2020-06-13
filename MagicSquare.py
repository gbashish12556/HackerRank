def formingMagicSquare(s):
    data = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]
    listSum = list()
    for i in data:
        sumNew = 0
        print(i)
        print(s)
        for j,k in zip(list(i),list(s)):
           for m,n in zip(list(j),list(k)):
             sumNew += max([m,n])-min([m,n])
        listSum.append(s)
    return min(listSum)


s = []

for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))

result = formingMagicSquare(s)