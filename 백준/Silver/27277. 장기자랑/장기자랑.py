import sys
input=sys.stdin.readline
n=int(input())
soldier=list(map(int,input().split()))
soldier.sort(reverse=True)
if n%2==1:
    n+=1
    soldier.insert(n//2,0)
s1=soldier[:n//2]
s2=soldier[n//2:][::-1]
place=[]
for i in range(n//2):
    place.append(s1[i])
    place.append(s2[i])
answer=place[0]
for i in range(1,n):
    answer+=max(0,place[i]-place[i-1])
print(answer)