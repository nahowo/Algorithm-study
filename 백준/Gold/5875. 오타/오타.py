import sys
input = sys.stdin.readline

def solution():
    s = input().rstrip()
    open = 0
    close = 0
    csum = 0

    for i in s:
        if i == '(':
            open += 1
            csum += 1
        else:
            close += 1
            csum -= 1
        if csum < 0: # 닫힌 게 더 많다면 그 이전까지의 닫힌 괄호를 하나씩 변환
            return close
        if csum == 1:
            open = 0

    return open # 열린 게 더 많다면 비정상 괄호가 열린 순간부터 마지막까지의 열린 괄호를 하나씩 변환
    
print(solution())