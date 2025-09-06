N, M = map(int, input().split())

def calc(a, b):
    ans = ((a+b) * (a-b))
    return ans

print(calc(N, M))