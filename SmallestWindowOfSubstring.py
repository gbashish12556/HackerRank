testCases = int(input())
for n in range(testCases):
    string1 = input()
    substring = input()
    lenString = len(string1)
    lenSubstring = len(substring)
    if lenString < lenSubstring:
        print("No such window")
    else:
        dict_sub = {}
        dict_str = {}

        for n in range(lenSubstring):
            if substring[n] in dict_sub.keys():
                dict_sub[substring[n]] += 1
            else:
                dict_sub[substring[n]] = 1
        count = 0
        start_index = 0
        min_length = 1000000
        for n in range(lenString):
            if string1[n] in dict_str.keys():
                dict_str[string1[n]] += 1
            else:
                dict_str[string1[n]] = 1
            if string1[n] in dict_sub.keys() and dict_str[string1[n]] == dict_sub[string1[n]]:
                count += 1
            print(dict_sub)
            print(dict_str)
            while string1[start_index] in dict_sub.keys() and string1[start_index] in dict_str.keys() and dict_str[string1[start_index]] > dict_sub[string1[start_index]] or string1[start_index] not in dict_sub.keys():
                dict_str[string1[start_index]] -= 1
                start_index += 1
            if count == len(dict_sub):
                if min_length > n - start_index+1:
                    min_length = n - start_index+1


        if count != len(dict_sub):
            print("No such window")
        else:
            print("Window is :"+string1[start_index:start_index+min_length])

