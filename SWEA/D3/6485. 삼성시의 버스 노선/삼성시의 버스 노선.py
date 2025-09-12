T = int(input())

for tc in range(1, T+1):
    n = int(input())

    route = []
    for _ in range(n):
        s, e = map(int, input().split())
        route.append((s, e))
    p = int(input())

    bus_stops = []
    for _ in range(p):
        bs = int(input())
        bus_stops.append(bs)

    check = [0] * 5001
    for s, e in route:
        for i in range(s, e+1):
            check[i] += 1

    check_bt = []
    for stop in bus_stops:
        check_bt.append(check[stop])

    print(f'#{tc}', *check_bt)