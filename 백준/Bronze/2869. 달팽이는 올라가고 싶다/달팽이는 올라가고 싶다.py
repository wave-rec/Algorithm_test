import math

# A: 낮에 올라가는 거리
# B: 밤에 미끄러지는 거리
# V: 총 막대 높이
A, B, V = map(int, input().split())

# 달팽이가 하루에 순수하게 올라가는 거리
daily_climb = A - B

# 마지막 날을 제외하고 올라가야 할 거리
# (V - B)는 마지막 날 밤에 미끄러지는 거리를 고려한 것
# A만큼 올라가면 정상에 도착하므로, 도착점(V)에서 밤에 미끄러지는 부분(B)까지를 먼저 계산
days = math.ceil((V - B) / daily_climb)

print(days)