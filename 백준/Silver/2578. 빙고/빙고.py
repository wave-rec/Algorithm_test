import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]

calls = []
for _ in range(5):
    calls += list(map(int, input().split()))

def mark(x):
    for i in range(5):
        for j in range(5):
            if board[i][j] == x:
                board[i][j] = 0
                return

def bingo_count():
    cnt = 0

    for i in range(5):
        ok = True
        for j in range(5):
            if board[i][j] != 0:
                ok = False
                break
        if ok:
            cnt += 1

    for j in range(5):
        ok = True
        for i in range(5):
            if board[i][j] != 0:
                ok = False
                break
        if ok:
            cnt += 1

    ok = True
    for i in range(5):
        if board[i][i] != 0:
            ok = False
            break
    if ok:
        cnt += 1

    ok = True
    for i in range(5):
        if board[i][4 - i] != 0:
            ok = False
            break
    if ok:
        cnt += 1

    return cnt

for k in range(25):         
    x = calls[k]
    mark(x)

    if bingo_count() >= 3:
        print(k + 1)        
        break