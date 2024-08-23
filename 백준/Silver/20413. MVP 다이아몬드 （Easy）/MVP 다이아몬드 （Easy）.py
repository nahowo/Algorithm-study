import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    s, g, p, d = map(int, input().split())
    level = input().rstrip()
    std = {'B': s - 1, 'S': g - 1, 'G': p - 1, 'P': d - 1, 'D': d}

    preSpend = 0
    totalSpend = 0
    for i in level:
        if i == 'D':
            tmp = d
            totalSpend += tmp
            preSpend = tmp
        else:
            tmp = std[i] - preSpend
            totalSpend += tmp
            preSpend = tmp
    return totalSpend

print(solution())