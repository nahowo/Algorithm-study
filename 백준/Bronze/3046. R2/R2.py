import sys
input = sys.stdin.readline

def solution():
    r1, s = map(int, input().split())
    return s + (s - r1)

print(solution())