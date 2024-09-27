import sys
from collections import deque
input = sys.stdin.readline
INF = 10 ** 9

def solution():
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    dp = [[INF] * (2 ** n) for _ in range(n)]
    cost = [INF for _ in range(n)]
    
    check = 1
    dp[0][check] = 0
    q = deque()
    q.append([0, check])

    while q:
        x, check = q.popleft()
        if check == (2 ** n) - 1:
            if board[x][0] != 0: # 이동 가능한 경로인 경우
                cost[x] = dp[x][check] + board[x][0]
            else:
                dp[x][check] = INF
        else:
            for i in range(1, n):
                if board[x][i] != 0 and check & (2 ** i) == 0:
                    if dp[x][check] + board[x][i] < dp[i][check | (2 ** i)]:
                        dp[i][check | (2 ** i)] = dp[x][check] + board[x][i]
                        q.append([i, check | (2 ** i)])
    
    return min(cost)

print(solution())