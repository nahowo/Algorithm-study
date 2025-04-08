import sys
input = sys.stdin.readline
LOG_M = 18

def fx(n, x):
    for i in range(LOG_M, -1, -1):
        if n >= 1 << i:
            n -= 1 << i
            x = table[x][i]
    return x

def solution():
    global table
    m = int(input())
    first = [0] + list(map(int, input().split()))
    table = [[first[i]] for i in range(m + 1)]

    for k in range(1, LOG_M + 1):
        for i in range(1, m + 1):
            table[i].append(table[table[i][k - 1]][k - 1])
    
    q = int(input())
    answer = [None] * q
    for i in range(q):
        n, x = map(int, input().split())
        answer[i] = str(fx(n, x))
    return '\n'.join(answer)

print(solution())