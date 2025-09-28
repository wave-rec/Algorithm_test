T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    best = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cur = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    cur += grid[k][l]

            if cur > best:
                best = cur

    print(f'#{tc} {best}')

