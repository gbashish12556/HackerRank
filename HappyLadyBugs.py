def happyLadybugs(b):
    b = list(b)
    dictionary = {}
    for x in  b:
        if x in dictionary:
            dictionary[x] +=1
        else:
            dictionary[x] = 1
    print(dictionary)
    if "_" in dictionary:
        for x in dictionary:
            if dictionary[x] == 1 and x != "_":
                return "NO"
    elif "_" not in dictionary:
            for i in range(len(b)):
                if i == 0:
                    if b[i] != b[i + 1]:
                        return "NO"
                elif i == len(b)-1:
                    if b[i] != b[i - 1]:
                        return "NO"
                elif b[i] != b[i-1] and b[i] != b[i+1]:
                    return "NO"
    return "YES"

b = "RBY_YBR"
print(happyLadybugs(b))