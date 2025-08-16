H, M = map(int, input().split())
time = int(input())

total_minutes = (H * 60) + M + time

final_H = (total_minutes // 60) % 24

final_M = total_minutes % 60

print(final_H, final_M)