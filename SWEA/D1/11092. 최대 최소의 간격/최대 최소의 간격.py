T = int(input())

for tc in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    min_num = min(numbers)
    max_num = max(numbers)

    min_idx = 0
    for i in range(n):
        if numbers[i] == min_num:
            min_idx = i + 1
            break

    max_idx = 0
    for i in range(n-1, -1, -1):
        if numbers[i] == max_num:
            max_idx = i + 1
            break

    ans = abs(max_idx - min_idx)
    print(f'#{tc} {ans}')