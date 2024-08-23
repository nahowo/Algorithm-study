import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    brand = list(map(int, input().split()))
    cnt = [0] * (m + 1)

    for i in brand:
        cnt[i] += 1
    
    return max(cnt)

print(solution())