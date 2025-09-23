T = int(input())

for tc in range(1, T+1):
    score = input().strip()
    total = 0
    streak = 0

    for ch in score:
        if ch == 'O':
            streak += 1
            total += streak
        else:
            streak = 0

    print(total)
