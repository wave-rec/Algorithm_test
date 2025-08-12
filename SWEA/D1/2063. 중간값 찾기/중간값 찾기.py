N = int(input())
arr = list(map(int, input().split()))
result = sorted(arr)

print(result[N//2])