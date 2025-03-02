import sys
input = sys.stdin.readline

def getGcd(a, b):
    while b:
        a, b = b, a % b
    return a

def getLcm(a, b):
    return (a * b) // getGcd(a, b)

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    numer = 1 # 분자
    denom = a[0] # 분모

    for i in range(1, n):
        n1, d1 = 1, a[i]
        lcm = getLcm(denom, d1)
        n1 = (lcm // denom) * numer + (lcm // d1) * n1
        d1 = lcm
        gcd = getGcd(n1, d1)
        numer = n1 // gcd
        denom = d1 // gcd

    return str(denom) + '/' + str(numer)
    
print(solution())