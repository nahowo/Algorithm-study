import sys
input = sys.stdin.readline

def solution():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    q = list(map(int, input().split()))

    dp = [0] * n
    for i in range(n):
        tmp = 1
        for j in range(i, i - 4, -1):
            tmp *= a[j]
        dp[i] = tmp
    total = sum(dp)
    for i in q:
        for j in range(4):
            ni = (i - 1 + j) % n
            dp[ni] *= -1
            total += 2 * dp[ni]
        print(total)
    return

solution()