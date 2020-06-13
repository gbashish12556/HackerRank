def permuteString(string1, left, right):
    if left == right:
        print(''.join(map(str,string1)))
    else:
        for x in range(left,right):
            string1[left],string1[x] = string1[x], string1[left]
            permuteString(string1, left+1,right)
            string1[left], string1[x] = string1[x], string1[left]

testCases = int(input())
for n in range(testCases):
    string1 = input()
    lenString  = len(string1)
    permuteString(list(string1),0,lenString)