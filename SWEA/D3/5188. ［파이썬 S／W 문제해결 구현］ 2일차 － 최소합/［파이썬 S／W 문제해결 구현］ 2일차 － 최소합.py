def plz(y, x, sm):
    global min_sum

    if sm >= min_sum:
        return

    if y == N-1 and x == N-1:
        min_sum = min(min_sum, sm)
        return

    if y + 1 < N:
        plz(y+1, x, sm + arr[y+1][x])

    if x + 1 < N:
        plz(y, x+1, sm + arr[y][x+1])

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('inf')

    plz(0, 0, arr[0][0])

    print(f'#{tc} {min_sum}')