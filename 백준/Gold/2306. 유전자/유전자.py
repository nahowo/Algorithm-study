import sys
input = sys.stdin.readline

def rec(s, e):
    if s >= e:
        return 0
    if s == e:
        return 1
    if cache[s][e] != -1:
        return cache[s][e]
    
    ret = -1
    if (dna[s] == 'a' and dna[e] == 't') or (dna[s] == 'g' and dna[e] == 'c'):
        ret = rec(s + 1, e - 1) + 2
    for k in range(s, e):
        ret = max(ret, rec(s, k) + rec(k + 1, e))

    cache[s][e] = ret
    return cache[s][e]

def solution():
    global dna, n, cache
    dna = input().rstrip()
    n = len(dna)
    cache = [[-1] * n for _ in range(n)]
    rec(0, n - 1)
    return cache[0][n - 1]
    
print(solution())