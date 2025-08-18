T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(input().strip())
    count_arr = [0] * 10


    for i in numbers:
        count_arr[int(i)] += 1

    max_num = 0
    max_num_count = 0

    for i in range (len(count_arr)):
        if count_arr[i] >= max_num_count:
            max_num_count = count_arr[i]
            max_num = i


    print(f'#{tc} {max_num} {max_num_count}')