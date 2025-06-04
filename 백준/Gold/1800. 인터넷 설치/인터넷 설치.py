import sys, heapq
input = sys.stdin.readline
MAX_SIZE = 10 ** 7

def dijkstra(target):
    dp = [[MAX_SIZE] * (k + 1) for _ in range(n + 1)]
    dp[1][k] = 0
    q = [[0, 1, k]] # 비용, 현재 노드 번호, 남은 무료 간선 수
    while q:
        cost, x, cnt = heapq.heappop(q)
        if x == n:
            continue
        for nx, ncost in graph[x].items():
            if ncost > target: # 현재 간선이 목표금액 target을 초과하면: 무료로 사용하는 간선 증가(즉 현재 간선은 무료로 사용)
                ncnt = cnt - 1
                ncost = cost
            else: # 아니라면: 무료가 아닌 간선을 최대치로 유지(즉 현재 간선은 돈을 내고 사용)
                ncnt = cnt
                ncost = max(cost, ncost)
            if ncnt < 0: # 무료 간선을 더 이상 사용할 수 없는 경우
                continue
            if dp[nx][ncnt] > ncost:
                dp[nx][ncnt] = ncost
                heapq.heappush(q, [ncost, nx, ncnt])
            
    return min(dp[n])

def solution():
    global graph, n, k
    n, p, k = map(int, input().split())
    graph = [dict() for _ in range(n + 1)]
    for _ in range(p):
        a, b, cost = map(int, input().split())
        graph[a][b] = cost
        graph[b][a] = cost
    
    # n까지 도달 가능한 최소 금액을 이분탐색
    start = 1
    end = 10 ** 6
    answer = MAX_SIZE
    while start <= end:
        mid = (start + end) // 2
        result = dijkstra(mid)
        if result < MAX_SIZE: # n까지 도달할 수 있다면 mid 감소
            end = mid - 1
            answer = min(answer, result)
        else: # 도달할 수 없다면 mid 증가
            start = mid + 1
    
    if answer < MAX_SIZE:
        return answer
    return -1
    
print(solution())