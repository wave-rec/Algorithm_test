T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    for _ in range(T):
        ans = A + B

    print(f"Case #{tc}: {A} + {B} = {ans}")