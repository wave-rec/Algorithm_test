T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]


    max_balloon_pop = 0
    dirs_plus = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(N):
        for j in range(M):
            power = grid[i][j]
            balloon_pop = grid[i][j]
            for di, dj in dirs_plus:
                for d in range(1, power+1):
                    ni, nj = i+ di*d, j+ dj*d
                    if 0 <= ni < N and 0 <= nj < M:
                        balloon_pop += grid[ni][nj]

            if max_balloon_pop < balloon_pop:
                max_balloon_pop = balloon_pop

    print(f'#{tc} {max_balloon_pop}')