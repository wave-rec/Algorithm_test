T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))

    max_one = 0
    count_one = 0
    for i in range(N):
        if numbers[i] == 1:
            count_one += 1

            if max_one < count_one:
                max_one = count_one

        else:
            count_one = 0

    print(f'#{tc} {max_one}')