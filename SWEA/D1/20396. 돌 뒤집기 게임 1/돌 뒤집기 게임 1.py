T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))

    for _ in range(M):
        i, j = list(map(int, input().split()))

        start = i - 1
        end = min(N, start + j)
        color = stones[start]
        
        stones[start: end] = [color] * (end - start)
        
    print(f"#{tc} {' '.join(map(str, stones))}")