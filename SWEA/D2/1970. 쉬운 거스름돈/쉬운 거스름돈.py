T = int(input())

for tc in range(1, T+1):
    money = int(input())
    sample = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    need = [0]*8

    for i in range (len(sample)):
        if money // sample[i] != 0:
            while money >= sample[i]:
                money -= sample[i]
                need[i] += 1
                
    print(f'#{tc}')
    print(*need)