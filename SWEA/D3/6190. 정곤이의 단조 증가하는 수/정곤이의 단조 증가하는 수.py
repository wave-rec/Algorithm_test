from itertools import combinations

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    multi = []
    for cb in combinations(numbers, 2):
        cur_num = cb[0] * cb[1]
        multi.append(cur_num)

    danjo = []
    for num in multi:
        s = str(num)

        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                break
        else:
            danjo.append(num)

    print(f'#{tc} {max(danjo) if danjo else -1}')