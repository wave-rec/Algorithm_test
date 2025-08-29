ans = []

for _ in range(5):
    N = int(input())
    ans.append(N)
    ans.sort()

print(int(sum(ans)/5))
print(ans[2])