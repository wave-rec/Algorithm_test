P, K = map(int, input().split())

count = 0
for increase in range(K, P+1):
    count += 1
    
print(count)