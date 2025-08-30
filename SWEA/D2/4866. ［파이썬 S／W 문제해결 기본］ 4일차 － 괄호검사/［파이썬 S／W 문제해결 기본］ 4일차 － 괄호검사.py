def check(arr):
    stack = []
    for i in arr:
        if i == '(':
            stack.append('(')
        elif i == '{':
            stack.append('{')
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return 0

    return 1 if not stack else 0


T = int(input())
for tc in range(1, T+1):
    arr = input()
    print(f'#{tc} {check(arr)}')
