import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    numbers = [input().rstrip() for _ in range(n)]
    alpha = dict()
    for number in numbers:
        for i, v in enumerate(number):
            alpha[v] = alpha.get(v, 0) + 10 ** (len(number) - i - 1)
    
    if len(alpha) == 10:
        tmpOrder = sorted(alpha.items(), key = lambda x: x[1])
        first = set()
        for number in numbers:
            first.add(number[0])
        for v in tmpOrder:
            if v[0] not in first:
                alpha[v[0]] = 0
                break

    order = sorted(alpha.items(), key = lambda x: -x[1])
    for i, v in enumerate(order):
        alpha[v[0]] *= (9 - i)
    
    return sum(alpha.values())

print(solution())