import sys
input = sys.stdin.readline
DIV = 10 ** 9 + 7

def solution():
    s = input().rstrip()
    l = len(s)
    answer = 0
    sqr = 1

    for i in range(l):
        if s[i] == 'O':
            answer += sqr % DIV
            answer %= DIV
        sqr *= 2 % DIV
    
    return answer

print(solution())