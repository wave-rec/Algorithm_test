from collections import deque

for _ in range(10) :
    tc = int(input())
    maze = [list(map(int, input().strip())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                end = (i, j)

    visited = [[0] * 16 for _ in range(16)]
    q = deque([start])
    visited[start[0]][start[1]] = 1

    dirs = [(1,0), (-1,0), (0,-1), (0,1)]

    found = 0
    while q:
        y, x = q.popleft()

        if maze[y][x] == 3:
            found = 1
            break

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx

            if 0 <= ny < 16 and 0 <= nx < 16:
                if maze[ny][nx] != 1 and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append((ny, nx))

    print(f'#{tc} {found}')
