import sys
input = sys.stdin.readline

def solution():
    answer = 0
    n = int(input())
    x = list(map(int, input().split()))
    pos = set(x)
    for s in range(n):
        for e in range(s + 1, n):
            if s == e:
                continue
            dist = abs(x[e] - x[s])
            if dist % 2:
                continue
            if max(x[s], x[e]) - dist // 2 in pos:
                answer += 1

    return answer

t = int(input())
for _ in range(t):
    print(solution())