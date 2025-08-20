from collections import deque
T = 10

for tc in range(1, T+1):
    tn = int(input())
    password = deque(map(int, input().split()))

    while password[-1] != 0:
        for i in range(1, 6):
            now = password.popleft() - i
            if now < 0:
                now = 0

            password.append(now)

            if now == 0:
                break

    print(f'#{tc}', *password)