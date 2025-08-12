T = int(input())

for tc in range(1, T+1):
    N = list(map(int, input().split()))
    
    result = []
    for i in N:
        if i % 2:
            result.append(i)
            
    print(f'#{tc} {sum(result)}')