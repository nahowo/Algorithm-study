import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    v = list(map(int, input().split()))
    v[n - 1] = 1 # 마지막 지점에서는 속도를 1로 낮춰야 함
    vSum = 1

    for i in range(n - 2, -1, -1):
        if v[i] > v[i + 1] + 1:
            v[i] = v[i + 1] + 1
        vSum += v[i]
    
    return vSum

print(solution())