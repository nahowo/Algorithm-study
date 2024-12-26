import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    memory = [0] + list(map(int, input().split()))
    cost = [0] + list(map(int, input().split()))
    c = sum(cost) + 1
    dp = [[0] * c for _ in range(n + 1)]
    minCost = sys.maxsize

    for i in range(1, n + 1):
        for j in range(c):
            tmpM = memory[i]
            tmpC = cost[i]

            if j < tmpC:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - tmpC] + tmpM, dp[i - 1][j])
            
            if dp[i][j] >= m:
                minCost = min(j, minCost)
    return minCost
    
print(solution())