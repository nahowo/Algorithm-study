import sys
input = sys.stdin.readline

def solution():
    h, w, x, y = map(int, input().split())
    bTable = [[0] * (w + 2 * y) for _ in range(h + 2 * x)]
    for i in range(h + x):
        tmp = list(map(int, input().split()))
        for j in range(w + y):
            bTable[i + x][j + y] = tmp[j]

    aTable = [[0] * (w + y) for _ in range(h + x)]
    for i in range(x, h + x):
        for j in range(y, w + y):
            aTable[i][j] = bTable[i][j] - aTable[i - x][j - y]

    answer = []
    for i in range(x, h + x):
        answer.append(' '.join(map(str, aTable[i][y : w + y])))
    return answer

result = solution()

for i in result:
    print(i)