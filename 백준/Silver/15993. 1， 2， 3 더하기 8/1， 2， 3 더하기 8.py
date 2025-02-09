import sys
input = sys.stdin.readline
DIV = 10 ** 9 + 9

def solution():
    t = int(input())
    numbers = [int(input()) for _ in range(t)]
    n = max(numbers)
    ev = [0] * (n + 4) # 짝
    od = [0] * (n + 4) # 홀
    
    ev[2] = 1
    ev[3] = 2
    od[1] = 1
    od[2] = 1
    od[3] = 2

    for i in range(4, n + 1):
        ev[i] = (od[i - 1] + od[i - 2] + od[i - 3]) % DIV
        od[i] = (ev[i - 1] + ev[i - 2] + ev[i - 3]) % DIV
        
    for i in range(t):
        print(od[numbers[i]], ev[numbers[i]])
    return

solution()