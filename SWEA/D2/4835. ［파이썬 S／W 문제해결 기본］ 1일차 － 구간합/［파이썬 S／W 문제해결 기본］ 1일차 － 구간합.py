T = int(input()) #테스트 케이스 개수
for tc in range(1, T+1): # 케이스 별로 돌면서
    N, M = map(int, input().split()) # 배열 길이, 연속으로 더할 개수 저장
    arr = list(map(int, input().split())) # 주어진 숫자 배열 리스트로 저장

    cur = sum(arr[0:M]) #첫 구간의 합을 구해서 cur에 저장
    max_cur = cur #여태 나온 값 중 최댓값
    min_cur = cur #여태 나온 값 중 최솟값

    for i in range(0, N - M + 1): #시작 인덱스를 처음부터 N-M까지 돌면서
        start = arr[i : i+M] #i번째 구간은 arr[i] 부터 arr[i+M]까지
        sum_cur = sum(start) #해당 구간의 합

        if sum_cur > max_cur: #해당하는 구간의 합이 여태 최댓값보다 크면
            max_cur = sum_cur #갱신

        if sum_cur < min_cur: #해당하는 구간의 합이 여태 최솟값보다 작으면
            min_cur = sum_cur #갱신

    print(f'#{tc} {max_cur - min_cur}') #최댓값 - 최솟값 출력