import sys
input = sys.stdin.readline

def makeTriangle(a, b, c): # a >= b >= c
    if a >= b + c:
        return -1
    return a + b + c

def solution():
    n = int(input())

    straw = []
    for _ in range(n):
        straw.append(int(input()))
    
    straw.sort(reverse = True)

    for i in range(n - 2):
        result = makeTriangle(straw[i], straw[i + 1], straw[i + 2])
        if result != -1:
            break
    
    return result

print(solution())