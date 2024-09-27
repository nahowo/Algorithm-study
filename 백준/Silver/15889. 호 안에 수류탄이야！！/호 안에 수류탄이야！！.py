import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    pos = list(map(int, input().split()))
    if n == 1:
        return 1
    
    p = list(map(int, input().split()))
    power = dict()
    end = max(pos) # 마지막 전우

    for i in range(n - 1):
        if pos[i] in power:
            if p[i] > power[pos[i]]:
                power[pos[i]] = p[i]
        else:
            power[pos[i]] = p[i]
    
    pos = list(power.keys()) + [end]
    pos.sort()
    n = len(pos)
    
    i = 0
    while i < n - 1:
        for j in range(1, n - i):
            if pos[i] + power[pos[i]] >= pos[i + j]:
                continue
            else:
                if j == 1:
                    return 0
                j -= 1
                break
        i += j
    return 1

if solution():
    print("권병장님, 중대장님이 찾으십니다")
else:
    print("엄마 나 전역 늦어질 것 같아")