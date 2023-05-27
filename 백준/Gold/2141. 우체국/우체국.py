import sys
input=sys.stdin.readline
n=int(input())
town=[]
people=0
for _ in range(n):
    a,b=map(int,input().split())
    town.append([a,b])
    people+=b
town.sort(key=lambda x:x[0])
mid=(people+1)//2
tmp=0
for i in range(n):
    tmp+=town[i][1]
    if tmp>=mid:
        print(town[i][0])
        break