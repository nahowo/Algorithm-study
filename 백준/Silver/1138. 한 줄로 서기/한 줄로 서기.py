import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    taller = list(map(int, input().split()))
    answer = [0] * n

    for i in range(n):
        fill(answer, taller[i], str(i + 1), n)
    return ' '.join(answer)

def fill(answer, leftTaller, person, n):
    cnt = 0
    for i in range(n):
        if answer[i] == 0:
            cnt += 1
            if cnt - 1 == leftTaller:
                answer[i] = person
                break

print(solution())