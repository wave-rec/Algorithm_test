T = int(input())

for tc in range(1, T+1):
    N = int(input())
    balloon_map = [list(map(int, input().split())) for _ in range(N)]

    max_score = 0
    for i in range(N):
        for j in range(N):
            row_score = sum(balloon_map[i])
            col_score = sum(balloon_map[r][j] for r in range(N))
            here = balloon_map[i][j]
            here_score = row_score + col_score - here


            if max_score < here_score:
                max_score = here_score

    print(f'#{tc} {max_score}')