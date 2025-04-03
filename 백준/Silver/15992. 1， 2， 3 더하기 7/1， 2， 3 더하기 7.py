import sys
input = sys.stdin.readline
DIV = 1000000009

def rec(n, m): # 남은 더할 수, 남은 숫자 사용 횟수
    if n < 0 or m < 0:
        return 0
    if cache[n][m] != -1:
        return cache[n][m]
    if m == 0:
        if n == 0:
            return 1
        return 0
    if m == 1 and n > 3:
        return 0
    
    ret = 0
    for i in range(1, 4):
        ret += rec(n - i, m - 1) % DIV
    cache[n][m] = ret % DIV
    return cache[n][m]

def solution():
    global cache
    t = int(input())
    testCase = [list(map(int, input().split())) for _ in range(t)]
    maxN = max(testCase[i][0] for i in range(t))
    maxM = max(testCase[i][1] for i in range(t))
    cache = [[-1] * (maxM + 1) for _ in range(maxN + 1)]
    answer = []
    for n, m in testCase:
        answer.append(rec(n, m))
    
    return '\n'.join(map(str, answer))

print(solution())