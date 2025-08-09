grid = [list(map(int, input().split())) for _ in range(9)]
biggest = 0
biggest_index = 0,0
for row in range(9):
    for col in range(9):
        if biggest <= grid[row][col]:
            biggest_index = row +1 , col +1
            biggest = grid[row][col]

print(biggest)
print(*biggest_index)