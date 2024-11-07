import sys
input = sys.stdin.readline

def solution():
    s = 0

    while True:
        x = int(input())
        if x != -1:
            s += x
        else:
            break
    return s

print(solution())