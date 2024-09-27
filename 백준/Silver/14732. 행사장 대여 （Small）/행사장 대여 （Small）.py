import sys
input = sys.stdin.readline

def solution():
    size = 501
    n = int(input())
    square = [[0] * (size) for _ in range(size)]
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        for j in range(x1, x2):
            for i in range(y1, y2):
                square[i][j] = 1
    
    answer = 0
    for i in range(size):
        for j in range(size):
            if square[i][j] == 1:
                answer += 1

    return answer

print(solution())