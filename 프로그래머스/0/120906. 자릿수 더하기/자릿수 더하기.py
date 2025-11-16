def solution(n):
    answer = 0
    
    n_string = str(n)
    for i in n_string:
        answer += int(i)
        
    return answer