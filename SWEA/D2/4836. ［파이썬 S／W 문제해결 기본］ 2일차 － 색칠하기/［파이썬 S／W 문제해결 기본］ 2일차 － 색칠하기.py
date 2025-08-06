T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if arr[i][j] != 0 and arr[i][j] != color:
                    arr[i][j] = 3
                else:
                    arr[i][j] = color

    purple = 0
    for r in arr:
        for c in r:
            if c == 3:
                purple += 1

    print(f'#{tc} {purple}')