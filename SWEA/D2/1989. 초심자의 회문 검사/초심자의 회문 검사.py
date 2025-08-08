T = int(input())

for tc in range(1, 1+T):
    word = input()
    reversed_word = word[::-1]
    result = 0
    if word == reversed_word:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')