T = int(input())

for tc in range(1, T+1):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    if int(month) > 12 or int(month) <= 0:
        print(f'#{tc} -1')

    elif int(month) == 2 and int(day) > 28:
            print(f'#{tc} -1')
    else:
        print(f'#{tc} {year}/{month}/{day}')