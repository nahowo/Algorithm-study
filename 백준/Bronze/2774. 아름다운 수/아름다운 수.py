import sys
input = sys.stdin.readline

def solution():
    x = input().rstrip()
    result = set(list(x))
    return len(result)

t = int(input())
for _ in range(t):
    print(solution())