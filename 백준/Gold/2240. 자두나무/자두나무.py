import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def rec(t, p, w):
    if w < 0:
        return 0
    if cache[t][p][w] != -1: # 메모이제이션
        return cache[t][p][w]
    if t == 1: # 1초에
        if p == 0: # 1번 나무
            cache[t][p][w] = tree[1][p]
            return cache[t][p][w]
        else: # 2번 나무
            if w > 0:
                cache[t][p][w] = max(tree[1])
            else:
                cache[t][p][w] = 0
            return cache[t][p][w]

    ret = tree[t][p] + max(rec(t - 1, p, w), rec(t - 1, (p + 1) % 2, w - 1))
    cache[t][p][w] = ret
    return ret

def solution():
    global t, cache, tree
    t, w = map(int, input().split())
    cache = [[[-1] * (w + 1) for _ in range(2)] for _ in range(t + 1)] # cache[t][p][w] = t시점에 p번 나무에 있을 때 이동횟수가 w번 남은 경우 얻을 수 있는 최대 자두
    tree = [[0, 0] for _ in range(t + 1)]
    for i in range(t):
        pos = int(input())
        tree[i + 1][pos - 1] = 1
    return max(rec(t, 0, w), rec(t, 1, w))

print(solution())