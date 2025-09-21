def plz(row, cost):
    global min_sum

    if cost >= min_sum:
        return

    if row == n:
        min_sum = min(min_sum, cost)
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            plz(row+1, cost+grid[row][i])
            visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n

    min_sum = float('inf')

    plz(0, 0)

    print(f'#{tc} {min_sum}')