def twoStacks(x, a, b):
  lenA = len(a)
  lenB = len(b)
  sumstack = []
  maxCount  = 0
  lenSumStack = 0
  sumOfSumStack =0
  for i in range(lenA):
      sumstack.append(a[i])
      lenSumStack +=1
      sumOfSumStack += a[i]
      if sumOfSumStack > x:
          sumOfSumStack -= sumstack.pop()
          lenSumStack -=1
          break
  countA = lenSumStack
  maxCount = countA
  for j in range(lenB):
      sumstack.insert(0, b[j])
      lenSumStack +=1
      sumOfSumStack += b[j]
      while sumOfSumStack > x and countA > 0:
          sumOfSumStack -= sumstack.pop()
          lenSumStack -=1
          countA -= 1
      if sumOfSumStack > x and countA == 0:
          sumstack = sumstack[1:]
          lenSumStack -=1
          break
      maxCount = max(maxCount, lenSumStack)
  maxCount = max(maxCount, lenSumStack)
  return maxCount
a = "1 1 0 0 1 0 1 0 0 1 0 0 1 1 1 0 0"
b = "0 0 0 0 0 1 0 1 1 0 1 1 0 1 0 1 1 0 0 0 0 0 0 1 0 1"
a = list(map(int, a.split(" ")))
b = list(map(int, b.split(" ")))
print(twoStacks(12,a,b))