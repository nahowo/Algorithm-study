import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    x = list(map(int, input().split()))
    csum = x.copy()
    for i in range(1, n):
        csum[i] += csum[i - 1]
    
    answer = 0
    for i in range(n):
        answer += x[i] * (csum[n - 1] - csum[i])
    return answer
    
print(solution())