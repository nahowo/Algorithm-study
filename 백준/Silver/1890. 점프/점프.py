import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def rec(i, j):
    if i >= n or j >= n:
        return 0
    if i == n - 1 and j == n - 1:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    
    if jump[i][j] == 0:
        ret = 0
    else:
        ret = rec(i + jump[i][j], j) + rec(i, j + jump[i][j])
    dp[i][j] = ret
    return ret

def solution():
    global dp, n, jump
    n = int(input())
    jump = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1] * (n) for _ in range(n)]
    
    return rec(0, 0)

print(solution())