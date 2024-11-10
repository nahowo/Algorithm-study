import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    cnt = dict()
    for _ in range(n * 10):
        tmp = list(map(int, input().split()))
        for i in range(5):
            cnt[tmp[i]] = cnt.get(tmp[i], 0) + 1
    
    result = []
    for k, v in cnt.items():
        if v > n * 2:
            result.append(k)
    result.sort()
    if len(result) == 0:
        print(-1)
    else:
        print(*result)

solution()