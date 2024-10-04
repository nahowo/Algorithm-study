import sys
input = sys.stdin.readline

def getPer(color, cnt, k):
    p = 1
    for i in range(k, 0, -1):
        p *= color / cnt
        color -= 1
        cnt -= 1

    return p

def solution():
    m = int(input())
    pebble = list(map(int, input().split()))
    k = int(input())
    totalP = sum(pebble)

    percentage = 0
    for i in pebble:
        percentage += getPer(i, totalP, k)
    
    return percentage

print(solution())