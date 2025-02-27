import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    counsel = [[0, 0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        t, p = map(int, input().split())
        counsel[i] = [t + i, p] # 종료일, 금액

    dp = [0] * (n + 2)
    
    for i in range(1, n + 2):
        dp[i] = dp[i - 1]
        for j in range(0, i):
            if counsel[j][0] == i: # 종료일이 오늘인 경우
                duration = counsel[j][0] - j
                dp[i] = max(dp[i], dp[i - duration] + counsel[j][1])

    return dp[n + 1]

print(solution())