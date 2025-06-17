import sys
input = sys.stdin.readline

def solution():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두 점이 일치하는 경우
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            return -1
        else:
            return 0
    
    dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
    add = (r1 + r2) ** 2
    sub = (r1 - r2) ** 2
    if dist == add or dist == sub:
        return 1
    elif sub < dist < add:
        return 2
    else:
        return 0

t = int(input())
answer = [''] * t
for i in range(t):
    answer[i] = str(solution())
print('\n'.join(answer))