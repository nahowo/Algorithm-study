import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    dp = [1] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(solution())