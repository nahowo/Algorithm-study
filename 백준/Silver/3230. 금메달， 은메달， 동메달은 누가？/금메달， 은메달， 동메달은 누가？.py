import sys
input=sys.stdin.readline
n,m=map(int,input().split())
line=[]
for i in range(1,n+1):
    place=int(input())
    line.insert(place-1,i)
line=line[:m][::-1]
answer=[]
for i in line:
    place=int(input())
    answer.insert(place-1,i)
for i in range(3):
    print(answer[i])