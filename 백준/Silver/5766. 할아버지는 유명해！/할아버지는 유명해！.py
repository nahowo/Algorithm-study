import sys
input = sys.stdin.readline

def solution(n, m):
    score = dict()
    check = [False] * 10001
    secondPlayers = []

    for _ in range(n):
        rank = list(map(int, input().split()))
        for i in range(m):
            score[rank[i]] = score.get(rank[i], 0) + 1

    scores = list(score.values())
    first = max(scores)
    scores.remove(first)
    second = max(scores)

    for k, v in score.items():
        if v == second:
            check[k] = True
    
    for i in range(10001):
        if check[i]:
            secondPlayers.append(i)

    return secondPlayers

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    print(*solution(n, m))