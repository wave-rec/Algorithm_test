T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = input()
    count = [0] * 10

    for number in numbers:
        count[int(number)] += 1

    max_count = max(count)

    max_num = 0
    for num in range(10):
        if count[num] == max_count:
            max_num = num

    print(f'#{tc} {max_num} {max_count}')