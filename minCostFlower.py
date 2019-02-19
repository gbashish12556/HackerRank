def getMinimumCost(k, c):
    c.sort(reverse=True)
    purchaseCount = [0]*k
    cost = 0;
    for i in range(len(c)):
         position = (i+1)%k-1
         purchaseCount[position] +=1
         cost += c[i]*purchaseCount[position]
    return cost

c = [1, 3, 5, 7, 9]
k = 3
print(getMinimumCost(k, c))
