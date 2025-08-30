def remove_dup(s: str) -> str:
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return ''.join(stack)

T = 10
for tc in range(1, T+1):
    N, M = input().split()
    ans = remove_dup(M)
    print(f'#{tc} {ans}')
