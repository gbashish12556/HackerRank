import math
def redJohn(n):

    count = 0

    if n < 4:
        return 0
    else:
        ways = [1]*(n+1)
        for i in range(4,n+1):
            ways[i] = ways[i-1]+(i//4)
        for num in range(2,ways[n]+1):
            if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
                count +=1
    return count

print(redJohn(8))