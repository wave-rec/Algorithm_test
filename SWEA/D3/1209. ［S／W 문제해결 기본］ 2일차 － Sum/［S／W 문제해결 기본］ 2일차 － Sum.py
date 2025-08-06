T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_row = 0
    for row in arr:
        sum_row = 0
        for cell in row:
            sum_row += cell
        max_row = max(sum_row, max_row)

    max_col = 0
    for col in range(100):
        sum_col = 0
        for row in range(100):
            sum_col += arr[row][col]
        max_col = max(max_col, sum_col)

    max_cross = 0
    left_cross = 0
    right_cross = 0
    for i in range(100):
        left_cross += arr[i][i]
        right_cross += arr[i][99-i]
    max_cross = max(left_cross, right_cross)

    result = max(max_row, max_col, max_cross)

    print(f'#{tc} {result}')