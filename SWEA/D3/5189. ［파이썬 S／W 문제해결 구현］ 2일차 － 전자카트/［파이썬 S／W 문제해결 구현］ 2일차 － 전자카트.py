def plz(cnt, cur_sum, y):
    global ans

    if cur_sum >= ans:
        return

    if cnt == N-1:
        ans = min(cur_sum + golf[y][0], ans)
        return

    for i in range(1,N):
        if not visited[i] and golf[y][i] > 0:
            visited[i] = 1
            plz(cnt+1, cur_sum + golf[y][i], i)
            visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    golf = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    visited[0] = 1
    ans = float('inf')

    plz(0, 0, 0)

    print(f'#{tc} {ans}')