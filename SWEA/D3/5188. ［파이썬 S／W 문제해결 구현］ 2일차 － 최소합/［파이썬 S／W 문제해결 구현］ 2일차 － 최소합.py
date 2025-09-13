direction = [(1, 0), (0, 1)]

def brute_force(y, x, sum_v):
    global result
    sum_now = sum_v + in_arr[y][x]

    if y == N-1 and x == N-1:
        if sum_now < result:
            result = sum_now
        return

    remain_steps = (N - 1 - y) + (N - 1 - x)
    lower_bound = sum_now + remain_steps * min_cell
    if lower_bound >= result:
        return

    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if ny < N and nx < N:
            brute_force(ny, nx, sum_now)


for tc in range(1, int(input()) + 1):
    N = int(input())
    in_arr = [list(map(int, input().split())) for _ in range(N)]

    result = 10**12
    min_cell = min(min(row) for row in in_arr)

    brute_force(0, 0, 0)
    print(f'#{tc} {result}')
