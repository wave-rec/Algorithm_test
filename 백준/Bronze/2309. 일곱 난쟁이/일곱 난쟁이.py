from itertools import combinations

dwarfs = [int(input()) for _ in range(9)]

for comb in combinations(dwarfs, 7):
    if sum(comb) == 100:
        for h in sorted(comb):
            print(h)
        break