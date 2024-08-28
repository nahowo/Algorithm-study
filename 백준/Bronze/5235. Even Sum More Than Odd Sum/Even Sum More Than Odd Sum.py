import sys
input = sys.stdin.readline

def printEmoji(e):
    return (":" + e + ":")

def solution():
    seq = list(map(int, input().split()))[1:]
    even = 0
    odd = 0

    for i in seq:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    if even > odd:
        return "EVEN"
    elif even < odd:
        return "ODD"
    else:
        return "TIE"

t = int(input())
for _ in range(t):
    print(solution())