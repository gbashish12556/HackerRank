testCases = int(input())
for n in range(testCases):
    string = input()
    dict = { "I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000 }
    lenString = len(string)
    val = 0
    for n in range(lenString):
        value  = dict[string[n]]
        if n < lenString-1:
            if dict[string[n]]< dict[string[n+1]]:
                value = value*(-1)
        val = val+value
    print(val)
