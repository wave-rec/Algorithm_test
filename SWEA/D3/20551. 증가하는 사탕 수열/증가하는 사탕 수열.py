T = int(input())

for tc in range(1, T+1):
    a, b, c = map(int, input().split())
    
    eat_count = 0

    if a < 1 or b < 2 or c < 3:
        print(f'#{tc} -1')
        continue
        
    if b >= c:
        eat_count += b - (c - 1)
        b = c - 1
        
    if a >= b:
        eat_count += a - (b - 1)
        a = b - 1
        
    print(f'#{tc} {eat_count}')