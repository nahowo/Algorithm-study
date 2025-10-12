import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    answer = []
    for i in range(n):
        answer.append(" " * (i) + "*" * (n - i))
    return "\n".join(answer)

print(solution())