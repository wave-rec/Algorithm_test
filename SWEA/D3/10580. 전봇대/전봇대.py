T = int(input())

for tc in range(1, T+1):
    n = int(input())
    
    wires = []
    ans = 0

    for _ in range(n):
        start, end = map(int, input().split())
        
        for prev_s, prev_e in wires:
            if start > prev_s and end < prev_e:
                ans += 1
                
        for prev_s, prev_e in wires:
            if start < prev_s and end > prev_e:
                ans += 1
                
        wires.append((start, end))
        
    print(f'#{tc} {ans}')