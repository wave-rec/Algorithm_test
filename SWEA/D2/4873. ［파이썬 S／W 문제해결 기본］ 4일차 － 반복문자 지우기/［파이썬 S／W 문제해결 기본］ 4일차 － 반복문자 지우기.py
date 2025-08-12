T = int(input())
for tc in range(1, T+1):
    txt = list(input())
    stack = []

    for i in txt:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    print(f'#{tc} {len(stack)}')