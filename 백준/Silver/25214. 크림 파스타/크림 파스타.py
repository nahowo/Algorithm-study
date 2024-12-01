import sys
input = sys.stdin.readline
MAX_SIZE = 10 ** 9 + 1

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * n

    tmpMin = a[0]
    for i in range(n):
        tmpMin = min(tmpMin, a[i]) # 현재까지 가장 작은 요소 업데이트
        dp[i] = max(dp[i - 1], a[i] - tmpMin)
    return dp

print(*solution())