import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = 1

    for i in range(n):
        if dp[i]:
            for j in range(i + 1, n):
                if not dp[j]:
                    if (j - i) * (1 + abs(a[j] - a[i])) <= k:
                        dp[j] = 1
    
    if dp[n - 1]:
        return "YES"
    return "NO"

print(solution())