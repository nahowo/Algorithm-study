import sys
input = sys.stdin.readline

def solution():
    n, l = map(int, input().split())
    al = 0
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    cnt = 0
    for i in range(n):
        a[i] = a[i]
        s[i] = s[i - 1] + a[i]
    s = [0] * l + s
    
    for i in range(l, l + n):
        tmp = s[i] - s[i - l]
        if 129 <= tmp and 138 >= tmp:
            cnt += 1

    return cnt

print(solution())