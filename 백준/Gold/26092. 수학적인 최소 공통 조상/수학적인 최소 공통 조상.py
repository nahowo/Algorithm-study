import sys
input = sys.stdin.readline

def getParent(n):
    parents = set([1, n])

    while n > 1:
        flag = False
        for i in range(2, int(n ** (1 / 2)) + 1):
            if n % i != 0:
                continue
            n //= i
            parents.add(n)
            flag = True
            break
        if not flag:
            break

    return parents

def solution():
    a, b = map(int, input().split())
    
    aParents = getParent(a)
    bParents = getParent(b)
    return max(aParents & bParents)

print(solution())