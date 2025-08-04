T = int(input()) # 테스트 케이스 개수를 받아서 정수형으로 변환

for tc in range(1, T+1): # 각 테스트 케이스를 순회
    N = int(input()) # 테스트 케이스 안에 요소를 받아서 정수형으로 변환
    nums = list(map(int, input().split())) # 공백을 기준으로 자른 후에 정수형으로 변환하고 map을 통해 list 형식으로 저장
    max_num = min_num = nums[0] # 가장 큰 숫자, 가장 작은 숫자 모두 첫 요소로 설정
    for x in nums[1:]: # 두 번째 요소부터 하나씩 꺼내서
        if x > max_num: # 만약 그 요소가 현재 최댓값보다 크면
            max_num = x # 갱신
        if x < min_num: # 만약 그 요소가 현재 최솟값보다 작으면
            min_num = x # 갱신

    print(f"#{tc} {max_num - min_num}") #가장 큰 값 - 가장 작은값 출력