T = int(input())
from collections import deque
for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    every = list(map(int, input().split()))
    for i in range(len(every)):
        every[i] = [i+1, every[i]]
    q_pizza = deque(every)
    q_fire = deque([q_pizza.popleft()])
    result = []
    while q_fire:
        if len(q_pizza) == 0:
            temp = q_fire.popleft()
            if temp[1] // 2 == 0:
                result.append(temp)
            else:
                temp[1] = temp[1] // 2
                q_fire.append(temp)
        elif len(q_fire)<N:
            q_fire.append(q_pizza.popleft())
        else:
            temp = q_fire.popleft()
            if temp[1] // 2 == 0:
                result.append(temp)
                q_fire.append(q_pizza.popleft())
            else:
                temp[1] = temp[1] // 2
                q_fire.append(temp)
    print(f"#{test_case} {result[-1][0]}")