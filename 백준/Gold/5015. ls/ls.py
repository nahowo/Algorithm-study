import sys
input = sys.stdin.readline

def recursion(w, s, file): # w는 와일드카드 시작 위치, s는 파일 시작 위치
    retw = w
    rets = s
    tp = p[w:]
    ts = file[s:]
    if cache[retw][rets] != -1:
        return cache[retw][rets]
    
    while w < W and s < S and p[w] == file[s]:
        w += 1
        s += 1
    
    if w == W:
        cache[retw][rets] = int(s == S)
        return cache[retw][rets]

    if p[w] == "*":
        for skip in range(0, S - s + 1):
            if recursion(w + 1, s + skip, file):
                return 1
    cache[retw][rets] = 0
    return cache[retw][rets]

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