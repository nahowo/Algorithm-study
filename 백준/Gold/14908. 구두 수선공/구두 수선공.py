import sys
from functools import cmp_to_key
input = sys.stdin.readline

def solution():
    n = int(input())
    ts = [list(map(int, input().split())) + [i + 1] for i in range(n)]
    ts.sort(key = cmp_to_key(compare))
    return ' '.join(map(lambda x: str(x[2]), ts))

def compare(j1, j2):
    r1 = j1[0] * j2[1]
    r2 = j2[0] * j1[1]
    if r1 < r2:
        return -1
    elif r1 > r2:
        return 1
    else:
        if j1[2] < j2[2]:
            return -1
        else:
            return 1

print(solution())