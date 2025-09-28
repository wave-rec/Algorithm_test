T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        A, B = B, A

    best = -20e8
    for start in range(M-N+1):
        cur_sum = 0
        for i in range(N):
            cur_sum += A[i] * B[start+i]

        if cur_sum > best:
            best = cur_sum
            
    print(f'#{tc} {best}')