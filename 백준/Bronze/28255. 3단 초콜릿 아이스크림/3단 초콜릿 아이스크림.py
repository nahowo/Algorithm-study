import sys, math
input = sys.stdin.readline

def a(s):
    n = len(s)
    sa = s[:math.ceil(n/3)]
    return sa

def rev(s):
    sr = ''
    for i in range(len(s) - 1, -1, -1):
        sr += s[i]
    return sr

def tail(s):
    st = s[1:]
    return st

def solution():
    s = input().rstrip()
    
    sa = a(s)
    if s == sa + rev(sa) + sa:
        return 1
    if s == sa + tail(rev(sa)) + sa:
        return 1
    if s == sa + rev(sa) + tail(sa):
        return 1
    if s == sa + tail(rev(sa)) + tail(sa):
        return 1
    return 0

t = int(input())
for _ in range(t):
    print(solution())