import sys
input = sys.stdin.readline

def solution():
    n, r = map(int, input().split())
    return n + (r * 2) - 1

print(solution())