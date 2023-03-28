import sys
input=sys.stdin.readline
n=int(input())
dots=[[] for _ in range(n+1)]
answer=0
for _ in range(n):
    x,y=map(int,input().split())
    dots[y].append(x)
for i in dots:
    i.sort()
    for j in range(1,len(i)-1):
        answer+=min((i[j]-i[j-1]),(i[j+1]-i[j]))
    try:
        answer+=i[1]-i[0]
        answer+=i[-1]-i[-2]
    except:
        continue
print(answer)