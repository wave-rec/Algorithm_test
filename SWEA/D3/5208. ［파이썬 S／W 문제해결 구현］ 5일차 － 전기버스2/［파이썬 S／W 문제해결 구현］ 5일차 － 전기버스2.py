def plz(cur, cnt):
    global min_change

    if cnt >= min_change:
        return

    if cur >= stops - 1:
        min_change = min(min_change, cnt)
        return

    max_jump = battery[cur]
    for step in range(1, max_jump + 1):
        plz(cur + step, cnt + 1)

T = int(input())

for tc in range(1, T + 1):
    info = list(map(int, input().split()))
    stops = info[0]
    battery = info[1:]

    if len(battery) < stops:
        battery += [0] * (stops - len(battery))

    min_change = float('inf')
    plz(0, -1)
    print(f'#{tc} {min_change}')