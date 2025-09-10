T = int(input())

def merge_sort(arr):
    global cnt
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 조건 체크: 왼쪽 마지막 > 오른쪽 마지막
    if left[-1] > right[-1]:
        cnt += 1

    # 두 배열 병합
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    sorted_arr = merge_sort(arr)

    print(f"#{tc} {sorted_arr[N//2]} {cnt}")
