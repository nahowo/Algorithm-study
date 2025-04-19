def getLine(h, n):
    line = [h + 1] * n
    for i in range(h, n):
        line[i] = i + 1
    return line

def solution(n, left, right):
    answer = []
    lh = left // n
    lw = left % n
    rh = right // n
    rw = right % n
    
    if lh == rh:
        answer += getLine(lh, n)[lw : rw + 1]
    else:
        answer += getLine(lh, n)[lw:]
        for i in range(lh + 1, rh):
            answer += getLine(i, n)
        answer += getLine(rh, n)[:rw + 1]
    
    return answer