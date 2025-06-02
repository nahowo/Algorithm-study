import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(1, n):
        a[i] += a[i - 1]
    a.sort(reverse = True)
    return sum(a[:k])

print(solution())