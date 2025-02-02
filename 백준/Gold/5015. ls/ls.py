import sys
input = sys.stdin.readline

def recursion(w, s, file): # w는 와일드카드 시작 위치, s는 파일 시작 위치
    if cache[w][s] != -1:
        return cache[w][s]
    
    if w < W and s < S and p[w] == file[s]:
        cache[w][s] = recursion(w + 1, s + 1, file)
        return cache[w][s]

    if w == W:
        cache[w][s] = int(s == S)
        return cache[w][s]

    if p[w] == "*":
        if recursion(w + 1, s, file):
            cache[w][s] = 1
            return cache[w][s]
        if s < S and recursion(w, s + 1, file):
            cache[w][s] = 1
            return cache[w][s]
    
    cache[w][s] = 0
    return cache[w][s]

def solution():
    global W, S, cache, p
    p = input().rstrip()
    W = len(p)
    n = int(input())

    for _ in range(n):
        file = input().rstrip()
        S = len(file)
        cache = [[-1] * (S + 1) for _ in range((W + 1))]
        if recursion(0, 0, file):
            print(file)

solution()