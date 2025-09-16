def Find(x):
    if parent[x] != 0:
        return Find(parent[x]) #재귀로 부모따라서 루트까지 올라감
    return x #0이면 x가 루트니까 x반환

def union(a, b): #루트 찾은 다음에 인덱스가 작은 쪽으로 합쳐주는 것
    a = Find(a)
    b = Find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    parent = [0]*(N+1) #모든 노드가 자기 자신이 루트인 상태

    for i in range(0, M*2, 2): #입력쌍 하나씩 꺼내오는 것
        if Find(lst[i]) != Find(lst[i+1]): #두 노드가 다른 집합이면 union으로 합침
            union(lst[i], lst[i+1])
            N -= 1 #합치면 남은 그룹 개수가 하나 줄어드는거니까 -1

    result = parent.count(0) #루트의 개수를 세는 것 근데 parent[0]은 0이니까 결과에서 하나 빼줘야됨 
    print(f'#{tc} {result-1}')