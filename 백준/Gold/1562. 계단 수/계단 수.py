import sys
input = sys.stdin.readline
DIV = 10 ** 9

def solution():
    n = int(input())
    if n < 10:
        return 0
    dp = [[[0] * (1024) for _ in range(10)] for _ in range(n + 1)]
    for k in range(1, 10):
        dp[0][k][1 << k] = 1
    
    for i in range(1, n):
        for k in range(10):
            for bit in range(1024): # 2 ** 10
                if k > 0:
                    dp[i][k][(bit) | (1 << k)] += (dp[i - 1][k - 1][bit]) % DIV
                if k < 9:
                    dp[i][k][(bit) | (1 << k)] += (dp[i - 1][k + 1][bit]) % DIV
    answer = 0
    for k in range(10):
        answer += (dp[n - 1][k][1023]) % DIV
    
    return answer % DIV

print(solution())