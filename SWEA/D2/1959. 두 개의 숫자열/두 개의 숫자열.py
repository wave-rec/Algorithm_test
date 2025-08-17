T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_num = 0
    if M > N:
        for i in range(M-N+1):
            total = 0
            for j in range(N):
                total += A[j] * B[i + j]

            if max_num < total:
                max_num = total

    else:
        for i in range(N-M+1):
            total = 0
            for j in range(M):
                total += A[i+j] * B[j]

            if max_num < total:
                max_num = total

    print(f'#{tc} {max_num}')