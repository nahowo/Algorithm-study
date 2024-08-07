import sys
input = sys.stdin.readline

def solution(a, b, c):
    s = set([a, b, c])
    a, b, c = sorted([a, b, c])
    if c >= a + b:
        return "Invalid"
    
    if len(s) == 1:
        return "Equilateral"
    elif len(s) == 2:
        return "Isosceles"
    else:
        return "Scalene"


while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    print(solution(a, b, c))