from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    
    for sx in range(n):
        if not visited[sx]:
            q = deque([sx])
            visited[sx] = True
            
            while q:
                x = q.popleft()
                for nx in graph[x]:
                    if not visited[nx]:
                        visited[nx] = True
                        q.append(nx)
            answer += 1
    
    return answer