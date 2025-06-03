import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    q = deque([0])
    dist = [-1] * (n + 1)
    dist[0] = 0
    
    while q:
        x = q.popleft()
        if x == n:
            break
        for nx in [x + 1, x + (x // 2)]:
            if nx <= n and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)
    if dist[n] <= k:
        return "minigimbob"
    return "water"

print(solution())