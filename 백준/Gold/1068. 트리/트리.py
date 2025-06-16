import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n = int(input())
    p = list(map(int, input().split()))
    graph = [set() for _ in range(n)] # graph[i]는 i 노드의 자식

    for i in range(n):
        if p[i] == -1:
            root = i
            continue
        graph[p[i]].add(i)
    
    toDelete = int(input())
    for i in range(n):
        if toDelete in graph[i]:
            graph[i].remove(toDelete)

    answer = 0
    q = deque([root])
    while q:
        x = q.popleft()
        if x != toDelete:
            if len(graph[x]) == 0:
                answer += 1
            for nx in graph[x]:
                q.append(nx)
    return answer

print(solution())