import sys
input = sys.stdin.readline
peter = [['.', '.', '#', '.'],
         ['.', '#', '.', '#'],
         ['#', '.', '.', '.'],
         ['.', '#', '.', '#'],
         ['.', '.', '#', '.']]

def wendy(pos):
    for nx, ny in [(0, pos), (1, pos - 1), (1, pos + 1), (2, pos - 2), (2, pos + 2), (3, pos - 1), (3, pos + 1), (4, pos)]:
        answer[nx][ny] = '*'

def solution():
    global answer
    word = input().rstrip()
    n = len(word)
    answer = ["" for _ in range(5)]
    for i in range(5):
        answer[i] = peter[i] * n
    for i in range(5):
        answer[i] += peter[i][0]

    for i, v in enumerate(word):
        if (i + 1) % 3 == 0:
            wendy(i * 4 + 2)
        answer[2][i * 4 + 2] = v

    result = ""
    for i in range(5):
        result += ''.join(answer[i]) + '\n'
    return result[:-1]

print(solution())