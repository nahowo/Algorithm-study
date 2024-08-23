import sys
input = sys.stdin.readline

def command(cmd):
    if cmd[0] == 1:
        x = cmd[1]
        w = cmd[2]
        d[w] = x
    else:
        w = cmd[1]
        print(d[w])
    return

def solution():
    global d
    n = int(input())
    d = dict()
    for _ in range(n):
        tmp = list(map(int, input().split()))
        command(tmp)
    return

solution()