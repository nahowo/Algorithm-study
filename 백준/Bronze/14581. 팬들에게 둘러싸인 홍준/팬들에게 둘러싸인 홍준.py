import sys
input = sys.stdin.readline

def printEmoji(e):
    return (":" + e + ":")

def solution():
    hongjun = input().rstrip()
    fan = "fan"
    print(printEmoji(fan) * 3)
    print(printEmoji(fan) + printEmoji(hongjun) + printEmoji(fan))
    print(printEmoji(fan) * 3)
    return

solution()