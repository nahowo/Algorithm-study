import sys
input = sys.stdin.readline

def isMutiple(n, i):
    if i % n == 0:
        return True
    return False

def solution():
    a, b = map(int, input().split())
    a, b = sorted([a, b]) # a <= b
    limit = a * b + 1
    
    for i in range(b, limit, b):
        if isMutiple(a, i):
            return i

t = int(input())
for _ in range(t):
    print(solution())