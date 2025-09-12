T = int(input())

for tc in range(1, T+1):
    n = int(input())
    one = input()

    new = one.split("0")
    one_sorted = []
    for ch in new:
        if ch != "":
            one_sorted.append(ch)
    
    ans = []
    for thing in one_sorted:
        ans.append(len(thing))
        
    print(f'#{tc} {max(ans)}')