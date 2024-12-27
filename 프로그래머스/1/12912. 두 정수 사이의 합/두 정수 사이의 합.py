def solution(a, b):
    answer = 0

    if a > b:
        a, b = b, a

    if (b - a) % 2 == 0:
        answer += (a + b) * (b - a) / 2 + (a + b) / 2
    else:
        answer += (a + b) * (b - a + 1) / 2
    
    return answer