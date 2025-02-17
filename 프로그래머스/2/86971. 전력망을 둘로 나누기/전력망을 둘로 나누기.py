from collections import deque

def bfs(removed, sx, graph, n):
    visited = [False] * (n + 1)
    visited[sx] = True
    visited[removed] = True
    q = deque([sx])
    cnt = 1
    
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                cnt += 1
                visited[nx] = True
                q.append(nx)
    return cnt

def solution(n, wires):
    answer = 100
    graph = [[] for _ in range(n + 1)]
    for i in range(len(wires)):
        graph[wires[i][0]].append(wires[i][1])
        graph[wires[i][1]].append(wires[i][0])
    
    for a, b in wires:
        tmp1 = bfs(a, b, graph, n)
        tmp2 = bfs(b, a, graph, n)
        answer = min(answer, abs(tmp1 - tmp2))
    
    return answer