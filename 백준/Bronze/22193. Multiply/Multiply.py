import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    a = int(input())
    b = int(input())
    answer = 0

    for i in range(n):
        ti = a % 10
        a = a // 10
        tmpb = b
        for j in range(m):
            tj = tmpb % 10
            tmpb = tmpb // 10
            answer += (ti * tj) * 10 ** (i + j)
    return answer

print(solution())