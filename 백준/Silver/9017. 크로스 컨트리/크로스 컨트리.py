import sys, heapq
input = sys.stdin.readline

def solution():
    n = int(input())
    num = list(map(int, input().split()))
    cnt = dict()
    score = dict()
    for i in range(n):
        cnt[num[i]] = cnt.get(num[i], 0) + 1
    cand = set()
    for k, v in cnt.items():
        if v == 6:
            cand.add(k)
            score[k] = []

    idx = 1
    for i in range(n):
        if num[i] in cand:
            score[num[i]].append(idx)
            idx += 1
    rank = sorted(list(score.items()), key = lambda x: (sum(x[1][:4]), x[1][4]))
    return rank[0][0]
    
t = int(input())
for _ in range(t):
    print(solution())