def solution(my_string, alp):
    answer = []
    for ch in my_string:
        if ch == alp:
            answer.append(alp.upper())
        else:
            answer.append(ch)
        result = "".join(answer)
    return result