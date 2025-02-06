import sys
input = sys.stdin.readline

def postOrder(n, si, ei):
    if si > ei or n >= N:
        return
    if si == ei:
        result.append(p[n])
        return
    postOrder(n + 1, si, inO[p[n]] - 1) # 왼쪽 자식 탐색
    leftCnt = inO[p[n]] - si
    postOrder(n + leftCnt + 1, inO[p[n]] + 1, ei) # 오른쪽 자식 탐색
    result.append(p[n])
    return

def solution():
    global N, preO, inO, visited, p, i, result
    N = int(input())
    p = list(map(int, input().split()))
    i = list(map(int, input().split()))
    preO = dict()
    inO = dict()
    for x in range(N):
        preO[p[x]] = x
        inO[i[x]] = x

    visited = [False] * (N + 1)
    result = []
    postOrder(0, 0, N - 1)
    print(*result)

t = int(input())
for _ in range(t):
    solution()