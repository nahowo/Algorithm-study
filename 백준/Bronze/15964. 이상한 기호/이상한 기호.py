import sys
input = sys.stdin.readline

def atSign(a, b):
    return (a + b) * (a - b)

def solution():
    a, b = map(int, input().split())
    return atSign(a, b)

print(solution())