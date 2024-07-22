import sys
input = sys.stdin.readline

def calc(k):
    return 5 + 2 * k

def solution():
    n, m = map(int, input().split())
    page = set(map(int, input().split()))
    prints = set(range(1, n + 1)) - page # 출력해야 하는 페이지

    if len(prints) == 0:
        return 0
    ink = 0
    
    s = -1
    e = 0
    for i in range(1, n + 1):
        if i in prints:
            if s == -1:
                s = i
                e = i
                continue
            
            if i - e > 3:
                ink += calc(e - s + 1)
                s = i
                e = i
            else:
                e = i
    ink += calc(e - s + 1)
    return ink

print(solution())