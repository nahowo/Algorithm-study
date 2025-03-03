import sys
input = sys.stdin.readline
INF = 10 ** 5

def solution():
    n = int(input())
    if n == 0:
        return 0
    request = [list(map(int, input().split())) for _ in range(n)]
    request.sort(key = lambda x: (-x[0], x[1]))
    schedule = [0] * ((max(request, key = lambda x: x[1]))[1] + 1)

    for i in range(n):
        pay = request[i][0]
        day = request[i][1]
        for j in range(day, 0, -1):
            if schedule[j] == 0:
                schedule[j] = pay
                break
    return sum(schedule)

print(solution())