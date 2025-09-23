from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, len(arr)+1):
    for ch in combinations(arr, i):
        if sum(ch) == S:
            cnt += 1

print(cnt)