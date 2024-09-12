import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    p = list(map(int, input().split()))
    prob = {i: [] for i in range(5)} # 0 ~ 4 레벨
    for _ in range(n):
        k, t = map(int, input().split())
        prob[k - 1].append(t)
    for i in range(5):
        prob[i].sort()

    # 무조건 적은 시간이 걸리는 문제를 푸는 게 이득
    minTime = 0
    for i in range(5):
        solve = prob[i][:p[i]]
        minTime += sum(solve)
        solve.append(solve[-1])
        for j in range(p[i]):
            minTime += solve[j + 1] - solve[j]
    
    return minTime + 60 * 4

print(solution())