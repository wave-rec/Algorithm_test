T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    stones = [list(input()) for _ in range(N)]

    found = False

    # 가로, 세로, 우하향, 좌하향 대각선 방향 벡터
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    # 모든 칸을 순회하며 검사 시작
    for r in range(N):
        for c in range(N):
            if stones[r][c] == 'o':
                for dr, dc in directions:
                    count = 1
                    # 현재 돌을 시작으로 4칸 더 탐색
                    for i in range(1, 5):
                        nr, nc = r + dr * i, c + dc * i

                        # 경계를 벗어나지 않고, 같은 돌인지 확인
                        if 0 <= nr < N and 0 <= nc < N and stones[nr][nc] == 'o':
                            count += 1
                        else:
                            break

                    if count >= 5:
                        found = True
                        break  # 방향 탐색 루프 탈출
                        

    if found:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')