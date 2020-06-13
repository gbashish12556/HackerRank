def biggerIsGreater(w):
    listChar = list(w)
    # listChar = map(lambda x:ord(x),listChar)
    lenString = len(w)
    for i in range(1,lenString):
        remaining = listChar[lenString-i:]
        characterValue = "z"
        for x in remaining:
            if ord(x) > ord(listChar[lenString-1-i]) and ord(x) < ord(characterValue):
                characterValue = x

        if ord(characterValue) > ord(listChar[lenString-1-i]):
            index = listChar[lenString-i:].index(characterValue)
            return w[:lenString-1-i]+characterValue+w[lenString-i:lenString-i+index]+w[lenString-i-1]+w[lenString-i+index+1:]

    return "no answer"

x = input()
print(biggerIsGreater(x))