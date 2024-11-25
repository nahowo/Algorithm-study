import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n + 1)]
    entry = [0] * (n + 1)
    basic = set([i for i in range(1, n)])

    for _ in range(m):
        x, y, k = map(int, input().split())
        graph[y].append([x, k])
        entry[x] += 1
        basic -= {x}
    
    parts = [[0] * (n + 1) for _ in range(n + 1)] # 부분 부품 정보
    q = deque(list(basic))
    
    while q:
        x = q.popleft()
        for nx, nCnt in graph[x]:
            if parts[x].count(0) == n + 1: # 기본 부품인 경우
                parts[nx][x] += nCnt
            
            else: # 중간 부품인 경우
                for i in range(1, n + 1):
                    parts[nx][i] += parts[x][i] * nCnt
            entry[nx] -= 1
            if entry[nx] == 0:
                q.append(nx)

    result = []
    for i in range(1, n):
        if i in basic:
            result.append([i, parts[n][i]])
    return result

answer = solution()
for i in answer:
    print(*i)