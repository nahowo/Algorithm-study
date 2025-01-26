import sys
input = sys.stdin.readline

def solution():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    cSum = [a[0]]
    answer = []

    for i in range(n):
        cSum.append(a[i] + cSum[i])
    
    for i in range(q):
        l, r = map(int, input().split())
        print(cSum[r] - cSum[l - 1])

solution()