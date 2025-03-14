import sys, bisect
input = sys.stdin.readline
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def getLis(arr):
    lis = [arr[0]]
    idxList = [0]
    cnt = 1
    for i in range(len(arr)):
        if lis[-1] < arr[i]:
            lis.append(arr[i])
            idxList.append(cnt)
            cnt += 1
        else:
            idx = bisect.bisect_left(lis, arr[i])
            lis[idx] = arr[i]
            idxList.append(idx)
        i += 1

    ret = set()
    cnt -= 1
    for v, i in enumerate(idxList[::-1]):
        if i == cnt:
            ret.add(len(arr) - v - 1)
            cnt -= 1
        if cnt < 0:
            break
    return ret, len(lis)

def solution():
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    lines.sort(key = lambda x: x[0])
    ret, l = getLis(list(lines[i][1] for i in range(n)))
    print(n - l)

    removeA = []
    for i in range(n):
        if i not in ret:
            removeA.append(str(lines[i][0]))
    
    return '\n'.join(removeA)

print(solution())