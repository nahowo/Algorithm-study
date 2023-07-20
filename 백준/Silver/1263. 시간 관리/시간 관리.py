import sys
input=sys.stdin.readline
n=int(input())
chore=[]
for _ in range(n):
    chore.append(list(map(int,input().split())))
chore.sort(key=lambda x:-x[1])
t=chore[0][1]-chore[0][0]
for i in range(1,n):
    if chore[i][1]>=t:
        t-=chore[i][0]
    else:
        t=chore[i][1]-chore[i][0]
    if t<0:
        t=-1
        break
print(t)