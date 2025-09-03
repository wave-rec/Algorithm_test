T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(A)
    count = 0

    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(A[i])
        if len(subset) == N and sum(subset) == K:
            count += 1

    print(f'#{tc} {count}')