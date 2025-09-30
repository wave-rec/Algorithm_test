def solution(a, b):
    if a >b:
        a, b = b, a
    lst = []
    for i in range(a, b+1):
        lst.append(i)
    answer = sum(lst)
    return answer