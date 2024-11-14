def solution(a, b):
    answer = 0
    l = len(a)
    for i in range(l):
        answer += a[i] * b[i]
        
    return answer