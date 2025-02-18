import sys
input = sys.stdin.readline

def getFactor(n):
    prime = [True] * (n + 1)
    prime[1] = False
    factor = [0] * (n + 1)
    for i in range(2, n + 1):
        if prime[i]:
            for j in range(i * 2, n + 1, i):
                factor[j] = i
                prime[j] = False
            factor[i] = i
    return factor
    

def solution():
    answer = 0
    n = int(input())
    k = int(input())
    factor = getFactor(n)
    for i in range(1, n + 1):
        if factor[i] <= k:
            answer += 1
    return answer

print(solution())