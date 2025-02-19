from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    lenCnt = dict()
        
    cnt = [-1] * (1 + n)
    cnt[1] = 0
    q = deque([1])
    maxLen = 0
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if cnt[nx] == -1:
                cnt[nx] = cnt[x] + 1
                maxLen = max(maxLen, cnt[nx])
                lenCnt[cnt[nx]] = lenCnt.get(cnt[nx], 0) + 1
                q.append(nx)
    answer = lenCnt[maxLen]
    
    return answer