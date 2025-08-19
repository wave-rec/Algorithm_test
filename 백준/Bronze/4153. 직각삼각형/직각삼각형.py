while True:
    A, B, C = map(int, input().split())

    list = [A, B, C]
    list.sort()
    big = list[2]

    if big != 0:
        if big**2 == list[0]**2 + list[1]**2:
            print('right')
        else:
            print('wrong')
            
    if A == B == C == 0:
        break