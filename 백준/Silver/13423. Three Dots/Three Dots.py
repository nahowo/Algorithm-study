import sys
input = sys.stdin.readline

def solution():
    global n, x
    answer = 0
    n = int(input())
    x = list(map(int, input().split()))
    for idx in range(n):
        answer += calcDist(idx)
    return answer

def calcDist(idx):
    count = 0
    dist = set()
    for i in range(n):
        if i == idx:
            continue
        d = abs(x[idx] - x[i])
        if d in dist:
            count += 1
        else:
            dist.add(d)
    return count

t = int(input())
for _ in range(t):
    print(solution())