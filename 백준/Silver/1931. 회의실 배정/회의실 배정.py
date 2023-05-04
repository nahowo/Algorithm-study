import sys
input=sys.stdin.readline
n=int(input())
meeting=[list(map(int,input().split())) for _ in range(n)]
meeting.sort(key=lambda x:(x[1],x[0])) #1. 회의가 일찍 끝나는 순, 2. 일찍 시작하는 순 정렬
last=0
count=0
for i,j in meeting:
    if i>=last:
        count+=1
        last=j
print(count)