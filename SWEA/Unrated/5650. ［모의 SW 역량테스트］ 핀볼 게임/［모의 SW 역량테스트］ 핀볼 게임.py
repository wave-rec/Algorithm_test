dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

change_dir = ((),
              (1, 3, 0, 2),
              (3, 0, 1, 2),
              (2, 0, 3, 1),
              (1, 2, 3, 0),
              (1, 0, 3, 2))

def play_game(r, c, d):
    global wormhole_info
    score = 0
    sr, sc = r, c      
    while True:
        r += dr[d]     
        c += dc[d]
        if (r, c) == (sr, sc) or A[r][c] == -1:
            return score
        if 1 <= A[r][c] <= 5:          
            d = change_dir[A[r][c]][d]
            score += 1
        elif 6 <= A[r][c] <= 10:  
            r, c = wormhole_info[(r, c)]

# main
T = int(input())
for tc in range(T):
    N = int(input())
    wormhole_check = [0] * 11
    wormhole_info = dict()  
    A = [[5] * (N+2)]   
    for i in range(1, N+1):
        A.append([5] + list(map(int, input().split())) + [5])
        for j in range(1, N+1):
            if 6 <= A[i][j] <= 10:
                num = A[i][j]
                if not wormhole_check[num]:
                    wormhole_check[num] = (i, j)
                else: 
                    wormhole_info[wormhole_check[num]] = (i, j)
                    wormhole_info[(i, j)] = wormhole_check[num]
    A.append([5] * (N+2))


    MAX = float('-inf')  
    for sr in range(1, N+1):
        for sc in range(1, N+1):
            if A[sr][sc] == 0:    
                for sd in range(4):
                    MAX = max(MAX, play_game(sr, sc, sd))
    print("#{} {}".format(tc+1, MAX))
