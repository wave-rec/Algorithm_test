import math

def bino_coef_factorial(n, k):
    ans = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    return ans

n, k = map(int, input().split())
print(bino_coef_factorial(n, k))

