import sys
input = sys.stdin.readline

def solution():
    cal = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    d = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    x, y = map(int, input().split())
    day = cal[x - 1] + y
    return d[day % 7]

print(solution())