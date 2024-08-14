import sys
input = sys.stdin.readline

def check(s1, s2, m):        
    for i in range(1, m + 1):
        if s2[m - i:] == s1[:i]:
            return True
    for i in range(m - 1, 0, -1):
        if s2[:i] == s1[m - i:]:
            return True
    return False

def solution():
    n, m = map(int, input().split())
    bottom = input().rstrip()
    for _ in range(n - 1):
        top = input().rstrip()
        if not check(bottom, top, m):
            return 0
        bottom = top
    return 1
    
print(solution())