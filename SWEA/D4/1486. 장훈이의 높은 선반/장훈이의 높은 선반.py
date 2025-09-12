def recur(cnt, total_height): #cnt = idx / 지금까지 선택한 사람들의 키 합
    global min_ans #현재까지 찾은 선반 이상 합의 최소값을 저장하는 전역 변수
    # 1) 목표(선반 높이) 이상이면 정답 후보 갱신 후 종료
    if total_height >= shelf_h:
        min_ans = min(min_ans, total_height) #가장 작은 합 유지
        return

    if total_height >= min_ans: #남은 사람을 다 더해도 선반에 못 미치면 끝
        return

    # 2) 모든 멤버를 다 고려했는데도 선반 미달이면 종료
    if cnt == members:
        return

    # 3) 현재 사람을 포함하는 경우
    recur(cnt + 1, total_height + heights[cnt])
    # 4) 현재 사람을 포함하지 않는 경우
    recur(cnt + 1, total_height)

T = int(input())

for tc in range(1, T+1):
    members, shelf_h = map(int, input().split())
    heights = list(map(int, input().split()))

    min_ans = 10000 * members

    recur(0, 0)

    print(f'#{tc} {min_ans - shelf_h}')
