import sys
input = sys.stdin.readline

def solution():
    n1, n2 = map(int, input().split())
    ants = [''] * (n1 + n2)
    g1 = input().rstrip()
    for i in range(n1 - 1, -1, -1):
        ants[i] = [g1[n1 - i - 1], 1]
    g2 = input().rstrip()
    for i in range(n1, n1 + n2):
        ants[i] = [g2[i - n1], -1]

    t = int(input())
    for _ in range(t):
        i = 0
        newAnts = ants.copy()
        while i < n1 + n2 - 1:
            d = ants[i][1]
            if 0 > i + d or n1 + n2 <= i + d:
                i += 1
                continue
            if ants[i][1] != ants[i + d][1]:
                newAnts[i], newAnts[i + d] = ants[i + d], ants[i]
                i += 2
            else:
                i += 1
        ants = newAnts.copy()
    return ''.join(map(lambda x: x[0], ants))

print(solution())