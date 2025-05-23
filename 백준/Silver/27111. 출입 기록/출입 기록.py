import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    check = set()
    answer = 0

    for _ in range(n):
        a, b = map(int, input().split())
        if b == 1:
            if a in check:
                answer += 1
            check.add(a)
        else:
            if a not in check:
                answer += 1
            else:
                check.remove(a)
    answer += len(check)
    return answer

print(solution())