def remove_dup(N):
    s = []
    for i in N:
        if s and s[-1] == i:  # 스택이 비어있지 않고, 마지막 문자랑 같으면
            s.pop()           # 제거
        else:
            s.append(i)       # 아니면 추가
    return len(s)


T = int(input())
for tc in range(1,T+1):
    N = input()
    print(f'#{tc} {remove_dup(N)}')