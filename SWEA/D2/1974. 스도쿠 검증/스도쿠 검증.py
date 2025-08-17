T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    find = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 0

    row = []
    for i in sudoku:
        row.append(i)

    for i in row:
        if sorted(i) == find:
            count = count + 1

    col_list = []
    for i in range(9):
        col = []
        for j in range(9):
            col.append(sudoku[j][i])
        col_list.append(col)

    for i in col_list:
        if sorted(i) == find:
            count = count + 1


    for i in range(0,9,3):
        for j in range(0,9,3):
            block_elements = []
            for k in range(3):
                for l in range(3):
                    block_elements.append(sudoku[i + k][j + l])

                if sorted(block_elements) == find:
                    count = count + 1


    if count == 27:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')



