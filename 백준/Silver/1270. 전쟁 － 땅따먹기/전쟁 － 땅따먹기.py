import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    answer = [''] * n

    for i in range(n):
        tmp = list(map(int, input().split()))
        answer[i] = check(tmp[0], tmp[1:])
    return '\n'.join(answer)

def check(t, army):
    count = dict()
    for i in range(t):
        count[army[i]] = count.get(army[i], 0) + 1
        if count[army[i]] > t / 2:
            return str(army[i])
    return "SYJKGW"

print(solution())