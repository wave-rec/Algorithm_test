def solve(num, charge, cnt):
    global ans

    if cnt > ans:
        return

    if num == N:
        if ans > cnt:
            ans = cnt
        return

    if charge < battery[num] and charge > 0:
        solve(num + 1, battery[num] - 1, cnt + 1)
        solve(num + 1, charge - 1, cnt)

    elif charge == 0:
        solve(num + 1, battery[num] - 1, cnt + 1)

    elif charge >= battery[num]:
        solve(num + 1, charge - 1, cnt)


T = int(input())

for tc in range(1, T + 1):
    ans = 1e9
    battery = list(map(int, input().split()))
    N = battery[0]
    solve(2, battery[1] - 1, 0)
    print(f'#{tc} {ans}')