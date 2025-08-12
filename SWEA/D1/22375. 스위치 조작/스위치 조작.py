T = int(input())

for tc in range(1, T+1):
    lights = int(input())
    now_lights = list(map(int, input().split()))
    after_lights = list(map(int, input().split()))

    change = 0
    for i in range(lights):
        if now_lights[i] != after_lights[i]:
            for j in range(i, lights):
                now_lights[j] = 1 - now_lights[j]

            change += 1

    print(f'#{tc} {change}')