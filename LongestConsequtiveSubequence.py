testCases = int(input())
for n in range(testCases):
    array = list(map(int,input().split(" ")))
    dict = {}
    max = 0
    for x in array:
        dict[x] = 1
    for x in dict.keys():
        count = 1
        current_index = x
        if x-1 not in dict.keys():
            while current_index+1 in dict.keys():
                current_index +=1
                count +=1
        if count>max:
            max = count
    print(max)