T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    fly_map = [list(map(int, input().split())) for _ in range(N)]

    max_flies = 0
    
    for top_r in range(N-M+1):
        for top_c in range(N-M+1):
            current_flies = 0
            
            for r in range(top_r, top_r + M):
                for c in range(top_c, top_c + M):
                    current_flies += fly_map[r][c]
                    
            if max_flies < current_flies:
                max_flies = current_flies

    print(f'#{tc} {max_flies}')


