T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    treasure = [list(map(int, input().split())) for _ in range(N)]

    max_row = 0
    for i in range(N):
        count_row = 0
        for j in range(M):
            if treasure[i][j] == 1:
                count_row += 1
            else:
                if count_row >= 2:
                    max_row = max(max_row, count_row)
                count_row = 0

        if count_row >= 2:
            max_row = max(max_row, count_row)



    max_col = 0
    for j in range(M):
        count_col = 0
        for i in range(N):
            if treasure[i][j] == 1:
                count_col += 1
            else:
                if count_col >= 2:
                    max_col = max(max_col, count_col)
                count_col = 0

        if count_col >= 2:
            max_col = max(max_col, count_col)



    result = max(max_row, max_col)

    print(f'#{tc} {result}')