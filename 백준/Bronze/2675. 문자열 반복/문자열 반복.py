T = int(input())

for _ in range(T):
    R, W = input().split()
    R = int(R)
    ans = ''
    for i in W:
        ans += i * R
    print(ans)