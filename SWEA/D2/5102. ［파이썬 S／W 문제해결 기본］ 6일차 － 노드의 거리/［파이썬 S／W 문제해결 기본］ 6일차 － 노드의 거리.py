T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    adjust_matrix = [[0] * (V+1) for _ in range (V+1)]

    for _ in range(E):
        n1, n2 = map(int, input().split())
        adjust_matrix[n1][n2] = 1
        adjust_matrix[n2][n1] = 1

    S, G = map(int, input().split())

    distance = [0] * (V+1)
    q = []

    distance[S] = 1
    q.append(S)

    result = 0

    while q:
        current_node = q.pop(0)
        
        if current_node == G:
            result = distance[current_node] - 1
            break

        for next_node in range(1, V+1):
            if adjust_matrix[current_node][next_node] == 1 and distance[next_node] == 0:
                distance[next_node] = distance[current_node] + 1
                q.append(next_node)

    print(f'#{tc} {result}')