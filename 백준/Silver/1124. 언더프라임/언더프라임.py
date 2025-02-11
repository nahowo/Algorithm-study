import sys
input = sys.stdin.readline

def getPrime():
    MAX = 10 ** 5 + 1
    prime = {i for i in range(2, MAX)}

    for i in range(2, int(MAX ** (1 / 2)) + 1):
        if i in prime:
            for j in range(i ** 2, MAX, i):
                if j in prime:
                    prime.remove(j)
    return prime

def factorize(n, prime):
    cnt = 0
    idx = 0
    while n > 1:
        if n % prime[idx] == 0:
            cnt += 1
            n //= prime[idx]
        else:
            idx += 1
    return cnt

def solution():
    a, b = map(int, input().split())
    prime = getPrime()
    primeL = sorted(list(prime))
    answer = 0
    for i in range(a, b + 1):
        if factorize(i, primeL) in prime:
            answer += 1
    return answer
    
print(solution())