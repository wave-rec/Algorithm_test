T = int(input())

for tc in range(1, 1+T):
    N, K = map(int, input().split())
    quiz_map = [list(map(int, input().split())) for _ in range(N)]
    length_of_quiz = 0

    # 가로
    for row in range(N):
        count = 0
        for col in range(N):
            if quiz_map[row][col] == 1:
                count += 1
            else:
                if count == K:
                    length_of_quiz += 1
                count = 0
        # 행 끝에서 한 번 더
        if count == K:
            length_of_quiz += 1

    # 세로
    for col in range(N):
        count = 0
        for row in range(N):
            if quiz_map[row][col] == 1:
                count += 1
            else:
                if count == K:
                    length_of_quiz += 1
                count = 0
        # 열 끝에서 한 번 더
        if count == K:
            length_of_quiz += 1

    # 출력
    print(f'#{tc} {length_of_quiz}')