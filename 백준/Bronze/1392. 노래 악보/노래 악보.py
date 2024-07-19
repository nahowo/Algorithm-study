import sys
input = sys.stdin.readline

def solution():
    n, q = map(int, input().split())
    b = []
    for i in range(1, n + 1):
        tmp = int(input())
        b.extend([i] * tmp)

    for _ in range(q):
        t = int(input())
        print(b[t])
    return

solution()