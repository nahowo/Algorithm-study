import sys
input = sys.stdin.readline

def solution():
    a, b = map(int, input().split())
    if (a * (100 - b)) >= 10000:
        return 0
    return 1

print(solution())