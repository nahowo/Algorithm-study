import sys
import heapq
input = sys.stdin.readline
toStr = lambda x: ''.join(map(str, x))

def change(s, a, b):
    s[a], s[b] = s[b], s[a]
    return s

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    result = toStr(sorted(a))
    start = toStr(a)
    m = int(input())
    operate = [list(map(int, input().split())) for _ in range(m)]
    cnt = dict()
    cnt[start] = 0
    visited = set()
    q = [[cnt[start], a]]

    while q:
        dist, x = heapq.heappop(q)
        xStr = toStr(x)
        if xStr in visited:
            continue
        for a, b, c in operate:
            nx = change(x.copy(), a - 1, b - 1)
            nxStr = toStr(nx)
            if nxStr not in visited:
                if nxStr in cnt:
                    cnt[nxStr] = min(cnt[nxStr], cnt[xStr] + c)
                else:
                    cnt[nxStr] = cnt[xStr] + c
                heapq.heappush(q, [cnt[nxStr], nx])
        visited.add(xStr)

    if result not in cnt:
        return -1
    return cnt[result]

print(solution())