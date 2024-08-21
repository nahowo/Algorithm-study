import sys
input = sys.stdin.readline

def left(length, l, c):
    return sum(l) - c * length

def slicing(length, l):
    cnt = 0

    for i in l:
        cnt += i // length

    return cnt

def solution():
    s, c = map(int, input().split())
    l = []
    for _ in range(s):
        l.append(int(input()))
    
    length = 0
    start = 1
    end = max(l)

    while start <= end:
        mid = (start + end) // 2
        tmp = slicing(mid, l)
        if tmp >= c:
            length = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return left(length, l, c)

print(solution())