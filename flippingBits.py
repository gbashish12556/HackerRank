def flippingBits(n):
    i = 31
    sum = 0;
    for i in range(32):
        sum += 1 * pow(2, i)
    return sum-n

print(flippingBits(9))
