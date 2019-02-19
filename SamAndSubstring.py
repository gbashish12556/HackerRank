# def substrings(n):
#     f =1
#     res = 0
#     MOD = pow(10,7)+7
#     lenN = len(n)
#     for j in range(lenN-1,-1,-1):
#         res =  (res+int(n[j])*f*(j+1))
#         f = (10*f + 1)
#     return res

def substrings(n):
    size = len(n)
    prev = int(n[0])
    total = prev
    for i in range (1, size):
        total= (total*10+int(n[i])*(i+1))%(10**9+7)
        prev = (total+prev)%(10**9+7)
    return prev


s = "1234567890"
print(substrings(s))