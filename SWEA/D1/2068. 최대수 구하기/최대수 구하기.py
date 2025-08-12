T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    
    max_number = arr[0]
    
    for i in arr:
        if i > max_number:
            max_number = i
            
    print(f'#{tc} {max_number}')