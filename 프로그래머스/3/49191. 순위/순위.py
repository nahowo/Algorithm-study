def dfs(x, graph, n):
    visited = [False] * (n + 1)
    q = [x]
    visited[x] = True
    cnt = 0
    
    while q:
        x = q.pop()
        for nx in graph[x]:
            if not visited[nx]:
                q.append(nx)
                visited[nx] = True
                cnt += 1
    return cnt

def solution(n, results):
    answer = 0
    graphF = [[] for _ in range(n + 1)]
    graphB = [[] for _ in range(n + 1)]
    match = [[0, 0] for _ in range(n + 1)] # win, lose
    for a, b in results:
        graphF[a].append(b)
        graphB[b].append(a)
    
    for i in range(1, n + 1):
        match[i][0] = dfs(i, graphF, n)
        match[i][1] = dfs(i, graphB, n)
    
    for i in range(1, n + 1):
        if sum(match[i]) == n - 1:
            answer += 1
    
    return answer