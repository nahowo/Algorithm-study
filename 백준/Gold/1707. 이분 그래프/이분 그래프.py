import sys
from collections import deque
input = sys.stdin.readline

def solution():
    v, e = map(int, input().split())
    graph = [set() for _ in range(v)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a - 1].add(b - 1)
        graph[b - 1].add(a - 1)
    
    vertices = [0] * v
    
    color = 1
    q = deque()
    for s in range(v):
        if vertices[s] == 0:
            q.append(s)
            vertices[s] = color
            while q:
                x = q.popleft()
                if vertices[x] == 0:
                    break
                for nx in graph[x]:
                    if vertices[nx] != 0:
                        if vertices[nx] == vertices[x]:
                            return "NO"
                        else:
                            continue
                    else:
                        vertices[nx] = -vertices[x]
                        q.append(nx)
    return "YES"

k = int(input())
for _ in range(k):
    print(solution())