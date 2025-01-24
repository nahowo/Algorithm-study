import sys
input = sys.stdin.readline
answer = {"T": "WINNER WINNER CHICKEN DINNER!", "F": "WHERE IS MY CHICKEN?"}

def solution():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    result = "F"
    try:
        if (y2 - y1) / (x2 - x1) != (y3 - y2) / (x3 - x2):
            result = "T"
    except:
        if x1 != x2 or x1 != x3 or x2 != x3:
            result = "T"
    return answer[result]

print(solution())