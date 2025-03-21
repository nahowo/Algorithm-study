import sys
input = sys.stdin.readline
DIV = 10

def solution():
    h, w = map(int, input().split())
    memo = [input().rstrip() for _ in range(h)]
    answer = 0
    for i in range(h):
        open = False
        for j in range(w):
            if memo[i][j] == '/':
                answer += 0.5
                open = not open
            elif memo[i][j] == '\\':
                answer += 0.5
                open = not open
            else:
                if open:
                    answer += 1
    return int(answer)
    
print(solution())