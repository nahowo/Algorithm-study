import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    answer = n
    j = 0
    i = 2
    while i < n:
        j = (n - 1) // ((n - 1) // i)
        num = 1 + (n - 1) // i
        answer += (j - i + 1) * num
        i = j + 1
    if n != 1:
        answer += 1
    return answer

print(solution())