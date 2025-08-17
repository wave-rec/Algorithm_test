T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = 0


    for i in puzzle:
        row_str = ''.join(map(str, i))
        gaps = row_str.split('0')

        for gap in gaps:
            if len(gap) == K:
                ans += 1


    for i in range(N):
        col = []
        for j in range(N):
            col.append(puzzle[j][i])

        col_str = ''.join(map(str, col))
        gaps = col_str.split('0')

        for gap in gaps:
            if len(gap) == K:
                ans += 1

    print(f'#{tc} {ans}')
