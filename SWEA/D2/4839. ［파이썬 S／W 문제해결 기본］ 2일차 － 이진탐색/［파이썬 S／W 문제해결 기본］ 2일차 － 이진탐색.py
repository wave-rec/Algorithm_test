T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    start = 1
    end = P
    A = 0

    while start <= end:
        middle = int((start+end)/2)
        A += 1
        if middle == Pa:
            break
        elif middle < Pa:
            start = middle
        elif middle > Pa:
            end = middle

    start = 1
    end = P
    B = 0

    while start <= end:
        middle = int((start + end) /2)
        B += 1
        if middle == Pb:
            break
        elif middle < Pb:
            start = middle
        elif middle > Pb:
            end = middle

    if A < B:
        print(f'#{tc} A')
    elif A > B:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')




