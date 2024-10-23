import sys
input = sys.stdin.readline

def getGcd(a, b):
    if a % b == 0:
        return b
    return getGcd(b, a % b)

def solution():
    a, b = map(int, input().split())
    return a * b // getGcd(a, b)

t = int(input())
for _ in range(t):
    print(solution())