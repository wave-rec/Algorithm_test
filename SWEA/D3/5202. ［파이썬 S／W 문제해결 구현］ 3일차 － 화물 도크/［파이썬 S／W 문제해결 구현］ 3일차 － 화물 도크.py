T = int(input())

for tc in range(1, T+1):
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]

    times.sort(key=lambda x: x[1])

    last = 0
    ans = 0
    for s, e in times:
        if last <= s:
            ans += 1
            last = e

    print(f'#{tc} {ans}')