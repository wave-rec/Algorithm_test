T = int(input())

for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split()))for _ in range(N)]

    sorted_info = sorted(info, key=lambda x: x[1])

    cnt = 0
    now = 0

    for i in range(N):
        s = sorted_info[i][0]
        e = sorted_info[i][1]
        if now <= s:
            cnt += 1
            now = e

    print("#{} {}".format(tc, cnt ))