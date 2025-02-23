import sys
input = sys.stdin.readline

def solution(n):
    p = [int(input()) for _ in range(n)]
    maxSum = -10000
    tmpSum = 0
    for i in range(n):
        if tmpSum + p[i] > p[i]:
            tmpSum += p[i]
        else:
            tmpSum = p[i]
        maxSum = max(maxSum, tmpSum)
    return maxSum

while True:
    n = int(input())
    if n == 0:
        break
    print(solution(n))