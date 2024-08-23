import sys
input = sys.stdin.readline

def solution(): # O(78498)
    s = int(input())
    for i in range(10 ** 6 + 1):
        if prime[i]:
            if s % i == 0:
                return "NO"
    return "YES"

prime = [True] * (10 ** 6 + 1)
prime[0] = False
prime[1] = False
for i in range(2, 10 ** 6 + 1):
    if prime[i]:
        for j in range(2, (10 ** 6 // i) + 1):
            prime[i * j] = False
# prime.count(True) => 78498

n = int(input())
for _ in range(n): # O(10)
    print(solution())