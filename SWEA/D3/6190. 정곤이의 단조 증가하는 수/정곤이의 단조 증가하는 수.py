from itertools import combinations

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    first = []
    for comb in combinations(numbers, 2):
        first.append(comb[0] * comb[1])

    danjo = []
    for number in first:
        s = str(number)
        ok = True
        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                ok = False
                break
        if ok:
            danjo.append(number)

    print(f'#{tc} {max(danjo) if danjo else -1}')




