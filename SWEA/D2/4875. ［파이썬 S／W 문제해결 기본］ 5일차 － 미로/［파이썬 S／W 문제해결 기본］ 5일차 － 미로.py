def escape():
    while s:
        a, b = s.pop()
        maze[a][b] = 1
        for w in range(4):
            c = a + dx[w]
            d = b + dy[w]

            if 0 <= c < N and 0 <= d < N:
                if maze[c][d] == 0:
                    s.append([c,d])
                    maze[c][d] = 1
                elif maze[c][d] == 3:
                    return 1
    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    s = []

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                s.append([i,j])
                break

    print(f'#{tc} {escape()}')

