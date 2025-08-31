def escape():
    while s:
        a, b = s.pop()
        maze[a][b] = 1

        for i in range(4):
            o = a + dx[i]
            p = b + dy[i]

            if 0 <= o < N and 0 <= p < N:
                if maze[o][p] == 0:
                    maze[o][p] = 1
                    s.append([o, p])
                elif maze[o][p] == 3:
                    return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    s = []

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                s.append([i, j])
                break

    print(f'#{tc} {escape()}')
