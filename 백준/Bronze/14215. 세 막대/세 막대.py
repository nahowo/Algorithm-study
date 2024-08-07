import sys
input = sys.stdin.readline

def solution():
    a, b, c = map(int, input().split())
    a, b, c = sorted([a, b, c])
    return a + b + min(c, a + b - 1)
    
print(solution())