T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    fly_map = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for top_r in range(N):
        for top_c in range(N):

            max_plus = 0

            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:  #위 아래 왼쪽 오른쪽 순서
                for catch in range(1, M):
                    ni, nj = top_r + di * catch, top_c + dj * catch
                    if 0 <= ni < N and 0 <= nj < N:
                        max_plus += fly_map[ni][nj]

            final_plus = max_plus + fly_map[top_r][top_c]

            cross_plus = 0

            for di, dj in [[-1, -1], [-1, 1], [1, 1], [1, -1]]:
                for catch in range(1, M):
                    ni, nj = top_r + di * catch, top_c + dj * catch
                    if 0 <= ni < N and 0 <= nj < N:
                        cross_plus += fly_map[ni][nj]

            final_cross = cross_plus + fly_map[top_r][top_c]

            result = max(result, final_cross, final_plus)

    print(f'#{tc} {result}')

