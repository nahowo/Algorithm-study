import sys
input = sys.stdin.readline

def prime_factorize(n):
    global factor, prime
    factor = [0] * (n + 1)
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, n + 1):
        if prime[i]:
            factor[i] = 1

            # 소수의 배수는 해당 소수를 인수로 가짐
            for j in range(2 * i, n + 1, i):
                prime[j] = False
                factor[j] += 1
            
            # 소수의 거듭제곱수는 해당 소수를 인수로 가짐
            sqr = i * i
            while sqr <= n:
                for j in range(sqr, n + 1, sqr):
                    factor[j] += 1
                sqr *= i

def solution():
    answer = 0
    a, b = map(int, input().split())
    prime_factorize(b)
    for i in range(a, b + 1):
        if prime[factor[i]]:
            answer += 1
    
    return answer
    
print(solution())