T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for _ in range(M):
        first_num = numbers[0]
        numbers.pop(0)
        numbers.append(first_num)

    print(f'#{tc} {numbers[0]}')