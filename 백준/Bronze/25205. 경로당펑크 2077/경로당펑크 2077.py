import sys
input = sys.stdin.readline
m = {'k', 'i', 'j', 'u', 'h', 'y', 'n', 'b', 'm', 'l', 'o', 'p'}

def solution():
    n = map(int, input())
    s = input().rstrip()

    return int(s[-1].lower() not in m)

print(solution())