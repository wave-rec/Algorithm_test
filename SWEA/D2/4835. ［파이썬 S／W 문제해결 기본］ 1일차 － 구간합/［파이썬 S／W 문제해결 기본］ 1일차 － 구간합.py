T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_sum = 0
    min_sum = 28e8
    
    for i in range(n-m+1):
        sum_cur = sum(numbers[i:i+m])
        
        if sum_cur > max_sum:
            max_sum = sum_cur
            
        if sum_cur < min_sum:
            min_sum = sum_cur
            
    print(f'#{tc} {max_sum-min_sum}')