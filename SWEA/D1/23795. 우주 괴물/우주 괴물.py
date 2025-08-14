T = int(input())

for tc in range(1, T+1):
    N = int(input())
    alien_map = [list(map(int, input().split())) for _ in range(N)]

    monster_i, monster_j = -1, -1

    for i in range(N):
        for j in range(N):
            if alien_map[i][j] == 2:
                monster_i, monster_j = i, j
                break

    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for di, dj in direction:
        ni, nj = monster_i + di, monster_j + dj

        while 0<= ni < N and 0<= nj < N:
            if alien_map[ni][nj] == 1:
                break

            if alien_map[ni][nj] == 0:
                alien_map[ni][nj] = 3

            ni += di
            nj += dj


    safe_area = 0
    for i in range(N):
        for j in range(N):
            if alien_map[i][j] == 0:
                safe_area += 1

    print(f'#{tc} {safe_area}')