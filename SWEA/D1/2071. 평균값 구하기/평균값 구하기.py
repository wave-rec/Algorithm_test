T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    print(f'#{tc} {round(float(sum(arr)/10))}')