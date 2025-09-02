T = int(input())

for tc in range(1, T+1):
    N = int(input())
    sales = list(map(int, input().split()))

    max_money = 0
    ans = 0

    for price in sales[::-1]:
        if price >= max_money:
            max_money = price
        else:
            ans += max_money - price

    print(f'#{tc} {ans}')