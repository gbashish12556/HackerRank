def kaprekarNumbers(p, q):
    result = []
    for i in range(p,q+1):
      lenstrI = len(str(i))
      strSquare = str(i**2)
      lenStrSqr = len(strSquare)
      if lenStrSqr > lenstrI:
          if int(str(strSquare)[-lenstrI:])+int(str(strSquare)[:len(strSquare)-lenstrI]) == i:
              result.append(i)
    print(" ".join(map(str,result)))

kaprekarNumbers(1, 100)