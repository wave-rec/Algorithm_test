import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
cnt = [0] * 10001

for _ in range(n):
    cnt[int(input())] += 1

for v in range(10001):
    c = cnt[v]
    for _ in range(c):      
        write(f"{v}\n") 
