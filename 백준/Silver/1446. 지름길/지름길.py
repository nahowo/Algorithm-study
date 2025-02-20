import sys
input = sys.stdin.readline

def solution():
    n, d = map(int, input().split())
    route = dict()
    for _ in range(n):
        s, e, l = map(int, input().split())
        if e in route:
            route[e].append([s, l])
        else:
            route[e] = [[s, l]]

    dp = [i for i in range(d + 1)]
    for i in range(1, d + 1):
        if i in route:
            for s, l in route[i]:
                dp[i] = min(dp[i], min(dp[i - 1] + 1, dp[s] + l))
        else:
            dp[i] = dp[i - 1] + 1

    return dp[d]
    
print(solution())