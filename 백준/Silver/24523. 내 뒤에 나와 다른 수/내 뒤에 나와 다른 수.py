import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    A = list(map(int, input().split()))
    d = [-1] * n

    j = n - 1
    for i in range(n - 2, -1, -1):
        if A[i] != A[j]:
            d[i] = j + 1
            j -= 1
        else:
            d[i] = d[j]
            j = i
    
    return d

print(*solution())