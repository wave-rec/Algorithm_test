T = int(input())

for tc in range(1, T+1):
    N = int(input())

    ans = []
    for _ in range(N):
        ch, n = input().split()
        ans.append(ch * int(n))

    new_ans = ''.join(ans)

    print(f"#{tc}")
    for i in range(0, len(new_ans), 10):
        print(new_ans[i:i+10])