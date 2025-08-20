from collections import deque
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    q = deque(numbers)

    for _ in range(M):
        q.append(q.popleft())

    print(f'#{tc} {q[0]}')