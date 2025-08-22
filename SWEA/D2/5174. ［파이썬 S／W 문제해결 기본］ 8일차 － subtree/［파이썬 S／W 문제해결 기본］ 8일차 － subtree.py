def subtree(T, left, right):
    if T == 0:
        return 0
    return 1 + subtree(left[T], left, right) + subtree(right[T], left, right)

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))
    root = N

    parent = [0] * (E + 2)
    left = [0] * (E + 2)
    right = [0] * (E + 2)

    for i in range(E):
        p, c = edge[i * 2], edge[i * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        parent[c] = p

    ans = subtree(root, left, right)

    print(f"#{tc} {ans}")