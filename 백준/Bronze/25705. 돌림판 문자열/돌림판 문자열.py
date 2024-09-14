import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    board = input().rstrip()
    check = set(list(board))
    m = int(input())
    s = input().rstrip()

    for i in range(m):
        if s[i] not in check:
            return -1
    
    cnt = 0
    a = n - 1 # 현재 위치

    for i in range(m):
        # 1
        a = (a + 1) % n
        cnt += 1
        # 2
        b = i # 가야 하는 문자열 위치
        while board[a] != s[b]:
            a = (a + 1) % n
            cnt += 1
        
    return cnt

print(solution())