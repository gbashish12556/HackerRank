def jumpingOnClouds(c, k):
    start = 0
    lenC = len(c)
    print(lenC)
    points = 100
    while points > 0:
        points -=1
        if c[start+k] == 1:
            points -=2
        if (start+k)%lenC == 0:
            break
            
    return points

c = "0 0 1 0 0 1 1 0"
c = c.split(" ")
jumpingOnClouds(c, 2)
