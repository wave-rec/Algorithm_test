n = int(input())
arr = list(input().split())

m = int(input())
arr2 = list(input().split())

set1 = set(arr)

for x in arr2:
    if x in set1:
        print(1)
    else:
        print(0)