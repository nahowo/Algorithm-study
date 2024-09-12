import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    dp = [0] * (max(arr) + 1)

    for i in range(1, n + 1):
        dp[arr[i]] = max(dp[arr[i]], dp[arr[i] - 1] + 1)
    
    return max(dp)

print(solution())