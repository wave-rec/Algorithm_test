n, k = map(int, input().split())
prices = []

for _ in range(n):
    coin = int(input())
    prices.append(coin)

prices.sort(reverse=True)

answer = 0
for coin in prices:
    if k >= coin:
        answer += k // coin
        k %= coin
        if k == 0:
            break

print(answer)