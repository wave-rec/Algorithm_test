T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    container.sort(reverse=True)
    truck.sort(reverse=True)

    c, t = 0, 0
    total = 0
    
    while t < m and c < n:
        if truck[t] >= container[c]:
            total += container[c]
            t += 1
        c += 1
        
    print(f'#{tc} {total}')