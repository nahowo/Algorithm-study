import sys
input = sys.stdin.readline

def solution():
    global n, snowball
    n = int(input())
    snowball = list(map(int, input().split()))
    snowball.sort()
    answer = 10 ** 9

    for a in range(n):
        for b in range(a + 1, n):
            elsa = snowball[a] + snowball[b]
            answer = min(answer, findAnna(elsa, a, b))
    return answer

def findAnna(elsa, a, b):
    c, d = getNext(-1, 1, a, b), getNext(n, -1, a, b)
    diff = 10 ** 9

    while c < d:
        anna = snowball[c] + snowball[d]
        diff = min(diff, getDiff(elsa, anna))
        if anna < elsa:
            c = getNext(c, 1, a, b)
        elif anna > elsa:
            d = getNext(d, -1, a, b)
        else:
            return 0
    return diff
        
def getNext(i, sign, a, b):
    i += sign
    while (i == a or i == b) and (i >= 0 and i < n):
        i += sign
    return i

def getDiff(x, y):
    return abs(x - y)

print(solution())