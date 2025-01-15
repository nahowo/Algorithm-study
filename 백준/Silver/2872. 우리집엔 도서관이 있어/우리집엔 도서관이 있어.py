import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    book = [int(input()) for _ in range(n)]
    
    cnt = 0
    current = n
    for i in range(n - 1, -1, -1):
        if book[i] == current:
            current -= 1
        else:
            cnt += 1

    return cnt
    
print(solution())