scores = []

for _ in range(5):
    score = int(input())

    if score >= 40:
        scores.append(score)
    else:
        scores.append(40)


ans = int(sum(scores) / len(scores))
print(ans)