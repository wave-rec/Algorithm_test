a = int(input())
b = int(input())
c = int(input())

val = str(a * b * c)

visited = [0] * 10

for i in val:
    j = int(i)
    visited[j] += 1

for k in visited:
    print(k)