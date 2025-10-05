while True:
    words = input().strip()
    if words == '0':
        break
    print('yes' if words == words[::-1] else 'no')
