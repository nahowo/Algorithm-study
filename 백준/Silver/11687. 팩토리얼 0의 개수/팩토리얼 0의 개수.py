import sys
input = sys.stdin.readline

def cntZero(n):
    cnt = 0
    while n >= 5:
        cnt += n // 5
        n //= 5
    return cnt

def solution():
    m = int(input())
    n = -1

    start = 1
    end = m * 5
    while start <= end:
        mid = (start + end) // 2
        tmp = cntZero(mid)
        if tmp < m:
            start = mid + 1
        elif tmp > m:
            end = mid - 1
        else:
            n = mid
            end = mid - 1
    return n
    
print(solution())