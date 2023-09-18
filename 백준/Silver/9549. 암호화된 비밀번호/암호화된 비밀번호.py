import sys
input=sys.stdin.readline
from collections import Counter
t=int(input())
def func(e,o):
    tmp_d=Counter(e[:len(o)])
    for i in range(len(e)-len(o)):
        first=e[i]
        last=e[i+len(o)]
        if tmp_d==d:
            return 1
        tmp_d[first]=tmp_d.get(first,0)-1
        tmp_d[last]=tmp_d.get(last,0)+1
        if tmp_d[first]==0:
            del tmp_d[first]
    return 0
for _ in range(t):
    encrypted=input()
    original=input().rstrip()
    d=Counter(original)
    if func(encrypted,original):
        print('YES')
    else:
        print('NO')