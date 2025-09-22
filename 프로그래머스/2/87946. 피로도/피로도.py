def solution(k, dungeons):
    n = len(dungeons)
    visited = [0] * n
    max_cnt = 0
    
    def backtrack(energy, count):
        nonlocal max_cnt
        max_cnt = max(max_cnt, count)

        for i in range(n):
            need, cost = dungeons[i]
            if not visited[i] and energy >= need:
                visited[i] = 1
                backtrack(energy - cost, count + 1)
                visited[i] = 0

    backtrack(k, 0)
    return max_cnt
