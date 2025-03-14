import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
DIV = 1000000007
maps = {}
maps[1] = [[0, 1, 0, 0, 0, 0, 0, 1],  
           [1, 0, 1, 0, 0, 0, 0, 1],  
           [0, 1, 0, 1, 0, 0, 1, 1],  
           [0, 0, 1, 0, 1, 0, 1, 0],  
           [0, 0, 0, 1, 0, 1, 0, 0],  
           [0, 0, 0, 0, 1, 0, 1, 0],  
           [0, 0, 1, 1, 0, 1, 0, 1],  
           [1, 1, 1, 0, 0, 0, 1, 0],]

def func(d, a, b):
    if d <= 1:
        return maps[d][a][b]
    
    maps.setdefault(d, [[0 for _ in range(8)] for _ in range(8)])
    if maps[d][a][b]:
        return maps[d][a][b]

    half1 = half2 = d // 2
    if d % 2 == 1:
        half2 += 1
    for k in range(8):
        maps[d][a][b] += func(half1, a, k) * func(half2, k, b)
        maps[d][a][b] %= DIV
    return maps[d][a][b]

def solution():
    d = int(input())
    return func(d, 0, 0)

print(solution())