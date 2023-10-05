import sys
from itertools import combinations
input=sys.stdin.readline
n=int(input())
g=[]
m=[]
tmp=0
for _ in range(n):
    f,c=map(int,input().split())
    tmp+=f
    g.append(f)
    m.append(c)
case=[]
money=[]
for i in range(1, len(g)):
    case.append(list(combinations(g,i)))
    money.append(list(combinations(m,i)))
m=int(input())
result=(10**9)+1
for i in range(m):
    v,t=map(int,input().split())
    if tmp*t<v:
        print('Case '+str(i+1)+": IMPOSSIBLE")
        result=(10**9)+1
        continue
    for j in range(len(case)):
        for k in range(len(case[j])):
            if sum(case[j][k])*t>v:
                result=min(sum(money[j][k]),result)
    print("Case "+str(i+1)+": "+str(result))