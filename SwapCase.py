def swap_case(s):
    string = '';
    for x in s:
        if x.islower():
            string += x.upper()
        else:
            string += x.lower()
    return string

s= 'HackerRank.com presents "Pythonist 2".'
print(swap_case(s))