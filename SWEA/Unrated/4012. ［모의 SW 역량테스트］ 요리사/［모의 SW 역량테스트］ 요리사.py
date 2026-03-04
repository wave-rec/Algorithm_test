from itertools import combinations

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]

    ingredients = list(range(n))
    half = n // 2

    best = 10**9

    def calc_team_score(team):
        score = 0
        for i in range(len(team)):
            for j in range(i + 1, len(team)):
                a = team[i]
                b = team[j]
                score += s[a][b] + s[b][a]
        return score

    all_a_teams = list(combinations(ingredients, half))

    for idx in range(len(all_a_teams) // 2):
        a_team = list(all_a_teams[idx])
        a_set = set(a_team)

        b_team = []
        for x in ingredients:
            if x not in a_set:
                b_team.append(x)

        a_score = calc_team_score(a_team)
        b_score = calc_team_score(b_team)

        diff = abs(a_score - b_score)
        if diff < best:
            best = diff

    print(f"#{tc} {best}")