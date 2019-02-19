def alternate(s):
    charSet = list(set(list(s)))
    maxCount = 0
    lenCharSet = len(charSet)
    for i in range(lenCharSet):
        for j in range(i+1,lenCharSet):
            setTwo = [charSet[i], charSet[j]]
            prev = ''
            count = 0
            newString = ''
            for x in s:
                if x in setTwo:
                    if x != prev:
                        newString += x
                        count +=1
                        prev = x
                    else:
                        count = 0
                        break
            if count > maxCount:
                maxCount = count
    return maxCount
s = "asvkugfiugsalddlasguifgukvsa"
print(alternate(s))