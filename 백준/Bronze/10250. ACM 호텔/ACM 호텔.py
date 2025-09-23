for _ in range(int(input())):
    H, W, N = map(int, input().split())
    x = N % H
    y = N // H + 1
    if x == 0:
        x = H
        y -= 1
    print(x * 100 + y)