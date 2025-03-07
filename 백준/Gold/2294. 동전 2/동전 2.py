import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    dp = [k + 1] * (k + 1)
    coins = set()
    for _ in range(n):
        a = int(input())
        if a <= k:
            dp[a] = 1
            coins.add(a)
    
    for i in range(1, k + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i - c] + 1)
    if dp[i] == k + 1:
        return -1
    return dp[k]
print(solution())