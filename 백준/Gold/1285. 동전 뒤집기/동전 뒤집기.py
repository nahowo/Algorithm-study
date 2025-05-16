import sys
input = sys.stdin.readline

def masking(row):
    for i in range(n):
        if row & (1 << i):
            board[i] = (1 << n) - board[i] - 1

def dfs(row):
    ret = 0
    masking(row)
    for i in range(n):
        cols = 0
        for j in range(n):
            if board[j] & (1 << i):
                cols += 1
        ret += min(cols, n - cols)
    masking(row)
    return ret

def solution():
    global n, board
    n = int(input())
    board = [0] * n
    for i in range(n):
        tmp = input().rstrip()
        for j in range(n):
            if tmp[j] == 'T':
                board[i] += (1 << j)

    answer = n ** 2
    for i in range(1 << n):
        answer = min(answer, dfs(i))
    return answer

print(solution())