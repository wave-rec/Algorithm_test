T = int(input())

for tc in range(1, T+1):
    N = int(input()) #배열 길이
    arr = list(map(int, input().split())) #배열
    result = []

    while arr:
        max_idx = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[max_idx]:
                max_idx = i
        result.append(arr.pop(max_idx))

        if not arr:
            break

        min_idx = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[min_idx]:
                min_idx = i
        result.append(arr.pop(min_idx))

    print(f'#{tc}', *result[:10])

