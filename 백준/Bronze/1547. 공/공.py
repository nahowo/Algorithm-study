import sys
input = sys.stdin.readline

def solution():
    m = int(input())
    cups = [-1, True, False, False]
    for _ in range(m):
        x, y = map(int, input().split())
        cups[x], cups[y] = cups[y], cups[x]
    
    return cups.index(True)

print(solution())