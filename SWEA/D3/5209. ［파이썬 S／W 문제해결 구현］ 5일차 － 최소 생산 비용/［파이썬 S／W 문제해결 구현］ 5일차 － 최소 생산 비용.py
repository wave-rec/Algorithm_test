def check(row, cost):
    global answer

    if row == n:
        answer = min(answer, cost)
        return

    if cost >= answer:
        return

    for j in range(n):
        if not visited[j]:
            visited[j] = True
            check(row+1, cost + factory[row][j])
            visited[j] = False

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    factory = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    answer = 1e9

    check(0, 0)

    print(f"#{tc} {answer}")