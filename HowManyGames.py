def howManyGames(p, d, m, s):
    count = 1
    s= s-p
    p = p - d
    while s > 0:
        if p > m:
            count +=1
            s = s-p
            print(str(s) + " : " + str(p) + " : " + str(count))
            p = p-d

        else:
            count += s//m+1
            s = 0
    return count-1
p= 16
d = 2
m = 1
s = 9981
print(howManyGames(p, d, m, s))