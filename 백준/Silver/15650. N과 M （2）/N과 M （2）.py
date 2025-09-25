from itertools import combinations

N, M = map(int, input().split())

arr = []
for i in range(1, N+1):
    arr.append(i)

lst = []
for nums in combinations(arr, M):
    lst.append(nums)

lst.sort(key=lambda x:nums[0])
for ans in lst:
    print(*ans)