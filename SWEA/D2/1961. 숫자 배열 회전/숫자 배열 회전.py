T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_map = [list(input().split()) for _ in range(N)]
    arr90 = []
    arr180 = []
    arr270 = []

    for i in range(N):
        value1 = []
        for k in range(N-1, -1, -1):
           value1.append(num_map[k][i])
        arr90.append(''.join(value1))


    for j in range(N-1, -1, -1):
        value2 = []
        for l in range(N-1, -1, -1):
            value2.append((num_map[j][l]))
        arr180.append(''.join(value2))

    for p in range(N-1, -1, -1):
        value3 = []
        for m in range(N):
            value3.append((num_map[m][p]))
        arr270.append(''.join(value3))


    print(f'#{tc}')
    for i in range(N):
        print(arr90[i], arr180[i], arr270[i])




