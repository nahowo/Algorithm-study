def solution(n):
    answer = 0
    bCnt = bin(n).count('1')
    nxt = n + 1
    while True:
        if bin(nxt).count('1') == bCnt:
            answer = nxt
            break
        nxt += 1
    return answer