def merge_the_tools(string, k):

    for i in range(0,len(string),k):
        subString = string[i:i+k]

        s = ''
        for x in subString:
            if x not in s:
                s +=x
        print(s)

string = "ABSCAAADD"
k = 3
merge_the_tools(string, k)