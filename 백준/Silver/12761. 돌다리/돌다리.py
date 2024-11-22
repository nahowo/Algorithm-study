import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    a, b, n, m = map(int, input().split())
    count = [0] * (100001)
    q = deque([])
    q.append(n)

    while q:
        x = q.popleft()
        if x == m:
            break
        for d in [-1, 1, -a, a, -b, b, x * (a - 1), x * (b - 1)]:
            nx = x + d
            if 0 <= nx and nx <= 10 ** 5 and count[nx] == 0:
                count[nx] = count[x] + 1
                q.append(nx)
    return count[m]

print(bfs())