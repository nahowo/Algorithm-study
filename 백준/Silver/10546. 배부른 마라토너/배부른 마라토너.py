import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    d = dict()
    for i in range(n):
        tmp = input().rstrip()
        d[tmp] = d.get(tmp, 0) + 1
    for i in range(n - 1):
        tmp = input().rstrip()
        d[tmp] -= 1
        if d[tmp] == 0:
            del d[tmp]
    return list(d.keys())[0]

print(solution())